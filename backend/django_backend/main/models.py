from django.db import models
from django.contrib.auth.models import AbstractUser


# Кастомная модель пользователя
class User(AbstractUser):
    ROLE_CHOICES = [
        ('creator', 'Создатель теста'),
        ('participant', 'Отвечающий'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='participant')  # Роль пользователя
    test_result = models.TextField(blank=True, null=True)  # Результаты тестов (можно расширить под конкретные данные)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# Модель теста
class Test(models.Model):
    title = models.CharField(max_length=255)  # Название теста
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tests')  # Создатель теста

    def __str__(self):
        return self.title


# Модель вопроса
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')  # Связь с тестом
    text = models.TextField()  # Текст вопроса

    def __str__(self):
        return self.text


# Модель варианта ответа
class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_options')  # Связь с вопросом
    text = models.CharField(max_length=255)  # Текст варианта ответа
    is_correct = models.BooleanField(default=False)  # Проверка правильности ответа

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Incorrect'})"


# Модель ответа участника
class ParticipantAnswer(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')  # Участник, дающий ответ
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='participant_answers')  # Вопрос
    selected_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE, related_name='chosen_answers')  # Выбранный ответ
    answered_at = models.DateTimeField(auto_now_add=True)  # Время ответа

    def __str__(self):
        return f"{self.participant.username} -> {self.question.text[:50]} -> {self.selected_option.text}"


