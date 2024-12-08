from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class AnonymousParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousParticipant
        fields = '__all__'


class AuthenticatedParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticatedParticipant
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class ParticipantAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantAnswer
        fields = '__all__'


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'


class TestLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestLink
        fields = '__all__'
