from django.db import models

from user.models import User


# Модель теста
class Test(models.Model):
    title = models.CharField(max_length=255)  # Название теста
    description = models.TextField(default="Тестирование")
    сreated_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    is_active = models.BooleanField(default=True)  # Активен ли тест
    is_anonymous = models.BooleanField(default=True)  # Флаг анонимности теста
    is_completed = models.BooleanField(default=False)  # Статус завершения теста
    default_time_limit = models.PositiveIntegerField(default=30,help_text="Default time limit for each question in seconds.")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tests')  # Создатель теста

    def complete(self):
        """
        Метод для завершения теста.
        """
        self.is_completed = True
        self.save()

    def __str__(self):
        return self.title


# Модель вопроса
class Question(models.Model):
    text = models.TextField(max_length=500)  # Текст вопроса
    order = models.PositiveIntegerField()  # Порядок вопроса в тесте
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')  # Связь с тестом

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['test', 'order'], name='unique_order_per_test')
        ]

    def save(self, *args, **kwargs):
        if not self.order:
            # Если порядок не задан, задаем его как последний в тесте
            max_order = Question.objects.filter(test=self.test).aggregate(max_order=models.Max('order'))['max_order']
            self.order = (max_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text


# Модель варианта ответа
class Answer(models.Model):
    text = models.CharField(max_length=255)  # Текст варианта ответа
    is_correct = models.BooleanField(default=False)  # Проверка правильности ответа
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')  # Связь с вопросом

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Incorrect'})"
