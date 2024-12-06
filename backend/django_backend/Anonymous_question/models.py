from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

import uuid


# Модель пользователя
class User(AbstractUser):
    # Переопределите поля, чтобы избежать конфликта имен с группами и правами
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Уникальное имя для обратной связи
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Уникальное имя для обратной связи
        blank=True,
    )

    def __str__(self):
        return self.username


# Модель теста
class Test(models.Model):
    title = models.CharField(max_length=255)  # Название теста
    description = models.TextField(default="Тестирование")
    сreated_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    is_active = models.BooleanField(default=True)  # Активен ли тест
    is_anonymous = models.BooleanField(default=True)  # Флаг анонимности
    default_time_limit = models.PositiveIntegerField(default=30,
                                                     help_text="Default time limit for each question in seconds.")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tests')  # Создатель теста

    def __str__(self):
        return self.title


# Модель участника
class AnonymousParticipant(models.Model):
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Уникальный идентификатор
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='anonymous_participants')  # Связь с тестом)

    def __str__(self):
        return f"Anonymous ({self.identifier}) -> {self.test.title}"


class AuthenticatedParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authenticated_participants')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_participations')  # Связь с тестом)

    def __str__(self):
        return f"{self.user.username} -> {self.test.title}"


# Модель вопроса
class Question(models.Model):
    text = models.TextField(max_length=500)  # Текст вопроса
    order = models.PositiveIntegerField()  # Порядок вопроса в тесте
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')  # Связь с тестом

    def __str__(self):
        return self.text


# Модель варианта ответа
class Answer(models.Model):
    text = models.CharField(max_length=255)  # Текст варианта ответа
    is_correct = models.BooleanField(default=False)  # Проверка правильности ответа
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')  # Связь с вопросом

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Incorrect'})"


# Модель ответа участника
class ParticipantAnswer(models.Model):
    selected_option = models.ForeignKey(Answer, on_delete=models.CASCADE,
                                        related_name='chosen_answers')  # Выбранный ответ
    answered_at = models.DateTimeField(auto_now_add=True)  # Время ответа
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='participant_answers')  # Вопрос

    anonymous_participant = models.ForeignKey(
        AnonymousParticipant,
        on_delete=models.CASCADE,
        related_name='answers',
        null=True,
        blank=True
    )
    authenticated_participant = models.ForeignKey(
        AuthenticatedParticipant,
        on_delete=models.CASCADE,
        related_name='answers',
        null=True,
        blank=True
    )

    def __str__(self):
        participant = self.anonymous_participant or self.authenticated_participant
        return f"{participant} -> {self.question.text[:50]} -> {self.selected_option.text}"


# Модель резульатата теста
class TestResult(models.Model):
    correct_answers = models.IntegerField(default=0)  # Количество правильных ответов
    total_questions = models.IntegerField(default=0)  # Всего вопросов
    completed = models.DateTimeField(auto_now_add=True)  # Дата завершения
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_results')  # Тест

    anonymous_participant = models.ForeignKey(
        AnonymousParticipant,
        on_delete=models.CASCADE,
        related_name='test_results',
        null=True,
        blank=True  # Поле можно оставить пустым для анонимных участников
    )
    authenticated_participant = models.ForeignKey(
        AuthenticatedParticipant,
        on_delete=models.CASCADE,
        related_name='test_results',
        null=True,
        blank=True,
    )

    def __str__(self):
        participant = self.anonymous_participant or self.authenticated_participant
        return f"{participant} -> {self.correct_answers}/{self.total_questions}"


# Модель генерирование ссылки для теста
class TestLink(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='links')

    def save(self, *args, **kwargs):
        if not self.test.is_active:
            raise ValueError("Не удается создать ссылку для неактивного теста")
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.link)
