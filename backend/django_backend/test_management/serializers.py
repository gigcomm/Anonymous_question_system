from rest_framework import serializers

from test_management.models import Test, Question, Answer

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError("Название теста не может быть пустым")
        if len(data.get('description', '')) > 500:
            raise serializers.ValidationError("Описание теста не должно превышать 500 символов")
        return data

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def validate_order(self, value):
        if value <= 0:
            raise serializers.ValidationError("Порядковый номер вопроса должен быть больше нуля")
        return value

    def validate_text(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("Текст вопроса не должен превышать 500 символов")
        return value

    def validate(self, data):
        if not data.get('test'):
            raise serializers.ValidationError("Каждый вопрос должен быть связан с тестом")
        return data

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    def validate_text(self, value):
        if not value:
            raise serializers.ValidationError("Текст ответа не может быть пустым")
        if len(value) > 255:
            raise serializers.ValidationError("Текст ответа не должен превышать 255 символов")
        return value

    def validate(self, data):
        if not data.get('question'):
            raise serializers.ValidationError("Каждый ответ должен быть связан с вопросом")
        return data