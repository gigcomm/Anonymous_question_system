from django.db import models
import uuid

from user.models import AnonymousParticipant, AuthenticatedParticipant
from test_management.models import Answer, Question

from test_management.models import Test

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

# Модель ответа участника
class ParticipantAnswer(models.Model):
    selected_option = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='chosen_answers')  # Выбранный ответ
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