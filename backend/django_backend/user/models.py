from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from rest_framework.exceptions import ValidationError


# Модель пользователя
class User(AbstractUser):

    def clean(self):
        if not self.email:
            raise ValidationError("Email обязателен для пользователя")
        if len(self.username) < 3:
            raise ValidationError("Имя пользователя должно содержать как минимум 3 символа")

    def __str__(self):
        return self.username
    
# Модель участника
class AnonymousParticipant(models.Model):
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Уникальный идентификатор
    test = models.ForeignKey('test_management.Test', on_delete=models.CASCADE, related_name='anonymous_participants')  # Связь с тестом)

    def clean(self):
        if not self.test:
            raise ValidationError("Участник должен быть связан с тестом")

    def __str__(self):
        return f"Anonymous ({self.identifier}) -> {self.test.title}"


class AuthenticatedParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authenticated_participants')
    test = models.ForeignKey('test_management.Test', on_delete=models.CASCADE, related_name='test_participations')  # Связь с тестом)

    def clean(self):
        if not self.user or not self.test:
            raise ValidationError("Участник должен быть связан с пользователем и тестом")

    def __str__(self):
        return f"{self.user.username} -> {self.test.title}"