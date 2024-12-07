from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from .models import *
from .serializers import *


# Представление для получения списка вопросов и создания нового вопроса


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TestAPIList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class AnonymousParticipantView(generics.ListCreateAPIView):
    queryset = AnonymousParticipant.objects.all()
    serializer_class = AnonymousParticipantSerializer


class AuthenticatedParticipantView(generics.ListCreateAPIView):
    queryset = AuthenticatedParticipant.objects.all()
    serializer_class = AuthenticatedParticipantSerializer


class QuestionAPIList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerAPIList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ParticipantAnswerAPIList(generics.ListCreateAPIView):
    queryset = ParticipantAnswer.objects.all()
    serializer_class = ParticipantAnswerSerializer


class TestResultAPIList(generics.ListCreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer


class TestLinkAPIList(generics.ListCreateAPIView):
    queryset = TestLink.objects.all()
    serializer_class = TestLinkSerializer
