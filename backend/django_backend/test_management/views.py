from django.shortcuts import render
from rest_framework import generics

from test_management.models import Test, Question, Answer
from test_management.serializers import TestSerializer, QuestionSerializer, AnswerSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TestAPIList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TestDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class QuestionAPIList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class QuestionDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AnswerAPIList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AnswerDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]