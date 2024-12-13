from django.db import models
import uuid

from rest_framework.exceptions import ValidationError

from test_management.models import Test

# Модель генерирование ссылки для теста
class TestLink(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='links')

    def clean(self):
        # Проверяем, активен ли тест
        if not self.test.is_active:
            raise ValidationError("Не удается создать ссылку для неактивного теста")

    def save(self, *args, **kwargs):
        # Вызываем валидацию перед сохранением
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.link)