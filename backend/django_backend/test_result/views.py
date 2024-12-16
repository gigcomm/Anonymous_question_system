from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from test_result.models import TestResult, ParticipantAnswer
from test_result.serializers import TestResultSerializer, ParticipantAnswerSerializer

class TestResultAPIList(generics.ListCreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TestResultDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ParticipantAnswerAPIList(generics.ListCreateAPIView):
    queryset = ParticipantAnswer.objects.all()
    serializer_class = ParticipantAnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ParticAnswerDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParticipantAnswer.objects.all()
    serializer_class = ParticipantAnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]