from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from test_link.models import TestLink

class TestLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestLink
        fields = '__all__'

    def validate_test(self, value):
        # Проверяем, активен ли тест
        if not value.is_active:
            raise serializers.ValidationError("Не удается создать ссылку для неактивного теста")
        return value