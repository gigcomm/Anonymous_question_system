from rest_framework import serializers

from test_result.models import TestResult, ParticipantAnswer


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'

    def validate(self, data):
        # Проверка, что указан только один тип участника
        if data.get('anonymous_participant') and data.get('authenticated_participant'):
            raise serializers.ValidationError("Только один тип участника может быть указан")
        if not data.get('anonymous_participant') and not data.get('authenticated_participant'):
            raise serializers.ValidationError("Должен быть указан хотя бы один тип участника")

        # Проверка, что количество правильных ответов не превышает общее количество вопросов
        if data.get('correct_answers', 0) > data.get('total_questions', 0):
            raise serializers.ValidationError(
                "Количество правильных ответов не может превышать общее количество вопросов")
        return data

class ParticipantAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantAnswer
        fields = '__all__'

    def validate(self, data):
        # Проверка, что указан только один тип участника
        if data.get('anonymous_participant') and data.get('authenticated_participant'):
            raise serializers.ValidationError("Только один тип участника может быть указан")
        if not data.get('anonymous_participant') and not data.get('authenticated_participant'):
            raise serializers.ValidationError("Должен быть указан хотя бы один тип участника")

        # Проверка, что выбранный ответ соответствует вопросу
        if data['selected_option'].question != data['question']:
            raise serializers.ValidationError("Выбранный ответ не соответствует указанному вопросу")
        return data
