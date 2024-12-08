from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser



# Модель пользователя
class User(AbstractUser):

    def __str__(self):
        return self.username
    
# Модель участника
class AnonymousParticipant(models.Model):
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Уникальный идентификатор
    from test_management.models import Test
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='anonymous_participants')  # Связь с тестом)

    def __str__(self):
        return f"Anonymous ({self.identifier}) -> {self.test.title}"


class AuthenticatedParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authenticated_participants')
    from test_management.models import Test
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_participations')  # Связь с тестом)

    def __str__(self):
        return f"{self.user.username} -> {self.test.title}"