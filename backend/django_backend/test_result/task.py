from celery import Celery

from django.db import transaction
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from test_result.models import TestResult, ParticipantAnswer
from user.models import AnonymousParticipant, AuthenticatedParticipant

app = Celery()

@app.task(bind=True)
def process_test_results(self, test_id):
    """
    Фоновая задача для обработки результатов теста.
    """
    from test_management.models import Test

    try:
        # Получение теста
        test = Test.objects.get(id=test_id)
    except Test.DoesNotExist:
        raise ValueError(f"Тест с идентификатором {test_id} не существует")

    # Определение является ли тест анонимным
    is_anonymous_test = test.is_anonymous

    if is_anonymous_test:
        # Включаем только анонимных участников
        participants = list(test.anonymous_participants.all())
    else:
        # Включаем только авторизованных участников
        participants = list(test.authenticated_participants.all())

    for participant in participants:
        # Определяем ответы для участника
        answers = ParticipantAnswer.objects.filter(
            test=test,
            anonymous_participant=participant if isinstance(participant, AnonymousParticipant) else None,
            authenticated_participant=participant if isinstance(participant, AuthenticatedParticipant) else None
        )

        correct_answers_count = 0
        total_questions = test.questions.count()

        # Проверяем правильность ответов
        for answer in answers:
            if answer.selected_option.is_correct:
                correct_answers_count += 1

        # Создаем результат теста
        with transaction.atomic():
            test_result = TestResult.objects.create(
                test=test,
                anonymous_participant=participant if isinstance(participant, AnonymousParticipant) else None,
                authenticated_participant=participant if isinstance(participant, AuthenticatedParticipant) else None,
                correct_answers=correct_answers_count,
                total_questions=total_questions
            )
            # Валидация и сохранение
            test_result.full_clean()
            test_result.save()

    if test.creator and test.creator.email:
        subject = f"Результаты теста: {test.title}"
        message = (
            f"Тест: {test.title}\n\n"
            f"Общее количество участников: {len(participants)}\n"
            f"Количество верных ответов: {correct_answers_count}/{total_questions}\n\n"
            "Результаты по каждому участнику можно найти в системе."
        )
        try:
            send_mail(
                subject,
                message,
                'iguly@yandex.ru',  # Установите свой адрес отправителя
                [test.creator.email],
                fail_silently=False,
            )
        except ValidationError as e:
            # Обработка ошибки при отправке email
            print(f"Failed to send email: {e}")

    return f"Обработаны результаты теста {test.title} для {len(participants)} участников."

