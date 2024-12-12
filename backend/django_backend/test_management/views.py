from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from test_management.models import Test, Question, Answer
from test_management.serializers import TestSerializer, QuestionSerializer, AnswerSerializer

class TestAPIList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class QuestionAPIList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerAPIList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer