from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import *

from test_link.models import TestLink
from test_link.serializers import TestLinkSerializer

class TestLinkAPIList(generics.ListCreateAPIView):
    queryset = TestLink.objects.all()
    serializer_class = TestLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TestLinkDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestLink.objects.all()
    serializer_class = TestLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]