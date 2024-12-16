from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import *

from test_link.models import TestLink
from test_link.serializers import TestLinkSerializer

class TestLinkAPIList(generics.ListCreateAPIView):
    queryset = TestLink.objects.all()
    serializer_class = TestLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TestLinkView(View):
    def get(self, request, link):
        test_link = get_object_or_404(TestLink, link=link)

        # Проверяем, активен ли тест
        if not test_link.test.is_active:
            return JsonResponse({"error": "Тест недоступен"}, status=403)

        # Возвращаем данные теста
        return JsonResponse({
            "test_id": test_link.test.id,
            "test_name": test_link.test.title,
        })


class TestLinkDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestLink.objects.all()
    serializer_class = TestLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]