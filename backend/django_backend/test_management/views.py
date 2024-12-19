from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import *

from test_management.models import Test, Question, Answer
from test_management.serializers import TestSerializer, QuestionSerializer, AnswerSerializer


@require_POST
def complete_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if not test.is_completed:
        test.complete()
    return JsonResponse({'status': 'success', 'message': 'Test completed!'})


class TestAPIList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Устанавливаем текущего пользователя как создателя теста
        serializer.save(creator=self.request.user)


class TestDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AllowAny]


class QuestionAPIList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]


class QuestionDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AllowAny]


class AnswerAPIList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AnswerDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
