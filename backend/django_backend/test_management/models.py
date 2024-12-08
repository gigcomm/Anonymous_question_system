from django.db import models

from user.models import User

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