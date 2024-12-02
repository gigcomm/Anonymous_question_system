from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

import uuid


# Кастомная модель пользователя
class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Уникальное имя для обратной ссылки
        blank=True,
        help_text="Группы, к которым принадлежит пользователь.",
        verbose_name="группы"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Уникальное имя для обратной ссылки
        blank=True,
        help_text="Разрешения, принадлежащие пользователю.",
        verbose_name="разрешения"
    )

    def __str__(self):
        return self.username


# Модель теста
class Test(models.Model):
    title = models.CharField(max_length=255)  # Название теста
    description = models.TextField(default="Тестирование")
    сreated_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    is_active = models.BooleanField(default=True)  # Активен ли тест
    is_anonymous = models.BooleanField(default=False)  # Флаг анонимности
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tests')  # Создатель теста

    def __str__(self):
        return self.title


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
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')  # Участник, дающий ответ
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='participant_answers')  # Вопрос

    def __str__(self):
        return f"{self.participant.username} -> {self.question.text[:50]} -> {self.selected_option.text}"


# Модель резульатата теста
class TestResult(models.Model):
    correct_answers = models.IntegerField(default=0)  # Количество правильных ответов
    total_questions = models.IntegerField(default=0)  # Всего вопросов
    completed = models.DateTimeField(auto_now_add=True)  # Дата завершения
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_results')  # Тест
    participant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='test_results',
        null=True,
        blank=True  # Поле можно оставить пустым для анонимных участников
    )
    participant_identifier = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Идентификатор участника для анонимных тестов (например, сессия)."
    )

    def __str__(self):
        if self.test.is_anonymous:
            return f"Anonymous -> {self.test.title} -> {self.correct_answers}/{self.total_questions}"
        return f"{self.participant.username} -> {self.test.title} -> {self.correct_answers}/{self.total_questions}"


# Модель генерирование ссылки для теста
class TestLink(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return str(self.link)
