from django.db import models
import uuid

from test_management.models import Test

# Модель генерирование ссылки для теста
class TestLink(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='links')

    def save(self, *args, **kwargs):
        if not self.test.is_active:
            raise ValueError("Не удается создать ссылку для неактивного теста")
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.link)