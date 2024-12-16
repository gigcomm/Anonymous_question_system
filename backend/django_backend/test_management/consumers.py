import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from test_management.models import Test
from user.models import AnonymousParticipant, AuthenticatedParticipant


class TestRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.test_link = self.scope['url_route']['kwargs']['test_link']
        self.room_group_name = f"test_{self.test_link}"

        # Получение теста из базы
        try:
            self.test = await asyncio.to_thread(Test.objects.get, link=self.test_link)
        except Test.DoesNotExist:
            await self.close(code=4001)  # Закрываем соединение, если тест не найден
            return

        # Проверка на тип участника в зависимости от is_anonymous
        if self.test.is_anonymous:
            self.participant = await asyncio.to_thread(
                AnonymousParticipant.objects.create, test=self.test
            )
            self.user_type = "anonymous"
            self.user_id = str(self.participant.identifier)
        elif not isinstance(self.scope["user"], AnonymousUser):  # Проверяем, что пользователь аутентифицирован
            self.participant = await asyncio.to_thread(
                AuthenticatedParticipant.objects.create, user=self.scope["user"], test=self.test
            )
            self.user_type = "authenticated"
            self.user_id = self.scope["user"].username
        else:
            await self.close(
                code=4002)  # Закрываем соединение, если тест не анонимный, а пользователь не аутентифицирован
            return

        # Добавление в группу WebSocket
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Уведомляем всех о новом участнике
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "user_joined",
                "user": self.user_id,
                "user_type": self.user_type,
            }
        )

        self.timer_task = None  # Переменная для отслеживания задачи таймера

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        if self.timer_task and not self.timer_task.done():
            self.timer_task.cancel()

    async def receive(self, text_data):
        data = json.loads(text_data)

        if data.get("type") == "start_question":
            if self.scope["user"].id == self.test.creator.id:  # Проверка, что это администратор
                question = data["question"]
                timer = data.get("timer", None)

                # Отменяем предыдущий таймер, если он был запущен
                if self.timer_task and not self.timer_task.done():
                    self.timer_task.cancel()

                if timer:
                    self.timer_task = asyncio.create_task(self.auto_switch_question(timer))

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {"type": "send_question", "question": question, "timer": timer}
                )
            else:
                await self.send(json.dumps({"error": "Вы не являетесь администратором"}))

        elif data.get("type") == "answer":
            answer = data["content"]
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "send_answer",
                    "user_id": self.user_id,
                    "user_type": self.user_type,
                    "answer": answer,
                }
            )

        elif data.get("type") == "next_question":
            # Логика ручного переключения вопросов
            if self.scope["user"].id == self.test.creator.id:
                next_question = data["next_question"]

                # Отменяем текущий таймер, если он есть
                if self.timer_task and not self.timer_task.done():
                    self.timer_task.cancel()

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {"type": "send_question", "question": next_question, "timer": None}
                )
            else:
                await self.send(json.dumps({"error": "Вы не являетесь администратором"}))

    async def auto_switch_question(self, timer):
        try:
            await asyncio.sleep(timer)
            # По истечении времени переключаем вопрос
            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "send_question", "question": "Следующий вопрос", "timer": None}
            )
        except asyncio.CancelledError:
            pass  # Таймер был отменен

    async def send_question(self, event):
        await self.send(text_data=json.dumps({
            "type": "question",
            "question": event["question"],
            "timer": event.get("timer", None)
        }))

    async def send_answer(self, event):
        user_display = (
            f"Аноним ({event['user_id'][:8]})"
            if event["user_type"] == "anonymous"
            else event["user_id"]
        )
        await self.send(text_data=json.dumps({
            "type": "answer",
            "user": user_display,
            "content": event["answer"]
        }))

    async def user_joined(self, event):
        await self.send(text_data=json.dumps({
            "type": "user_joined",
            "user": event["user"],
            "user_type": event["user_type"]
        }))