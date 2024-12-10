from rest_framework import serializers

from test_result.models import TestResult, ParticipantAnswer


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'

class ParticipantAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantAnswer
        fields = '__all__'

    def validate(self, data):
        if data.get('anonymous_participant') and data.get('authenticated_participant'):
            raise serializers.ValidationError("Only one participant type can be specified.")
        if not data.get('anonymous_participant') and not data.get('authenticated_participant'):
            raise serializers.ValidationError("One participant type must be specified.")
        return data
