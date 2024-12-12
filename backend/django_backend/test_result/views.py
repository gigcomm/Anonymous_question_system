from django.shortcuts import render
from rest_framework import generics

from test_result.models import TestResult, ParticipantAnswer
from test_result.serializers import TestResultSerializer, ParticipantAnswerSerializer

class TestResultAPIList(generics.ListCreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer


class ParticipantAnswerAPIList(generics.ListCreateAPIView):
    queryset = ParticipantAnswer.objects.all()
    serializer_class = ParticipantAnswerSerializer