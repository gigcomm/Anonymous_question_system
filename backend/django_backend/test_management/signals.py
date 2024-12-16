from django.db.models.signals import post_save
from django.dispatch import receiver
from test_management.models import Test
from test_result.task import process_test_results

@receiver(post_save, sender=Test)
def handle_test_completion(sender, instance, **kwargs):
    if instance.is_completed:  # Проверяем статус завершения
        process_test_results.apply_async(args=[instance.id])
