from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


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
    test_result = models.TextField(blank=True, null=True)  # Результаты тестов (можно расширить под конкретные данные)

    def __str__(self):
        return self.username


# Модель теста
class Test(models.Model):
    title = models.CharField(max_length=255)  # Название теста
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tests')  # Создатель теста
    сreated_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    is_active = models.BooleanField(default=True)  # Активен ли тест

    def __str__(self):
        return self.title


# Модель вопроса
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')  # Связь с тестом
    text = models.TextField()  # Текст вопроса
    order = models.PositiveIntegerField()  # Порядок вопроса в тесте

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
    selected_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE,
                                        related_name='chosen_answers')  # Выбранный ответ
    answered_at = models.DateTimeField(auto_now_add=True)  # Время ответа

    def __str__(self):
        return f"{self.participant.username} -> {self.question.text[:50]} -> {self.selected_option.text}"


# Модель резульатата теста
class TestResult(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results')  # Участник
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_results')  # Тест
    score = models.IntegerField(default=0)  # Баллы за тест
    correct_answers = models.IntegerField(default=0)  # Количество правильных ответов
    total_questions = models.IntegerField(default=0)  # Всего вопросов
    completed = models.DateTimeField(auto_now_add=True)  # Дата завершения

    def __str__(self):
        return f"{self.participant.username} -> {self.test.title} -> {self.score}"
