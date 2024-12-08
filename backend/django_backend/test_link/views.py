from django.shortcuts import render
from rest_framework import generics

from test_link.models import TestLink
from test_link.serializers import TestLinkSerializer

class TestLinkAPIList(generics.ListCreateAPIView):
    queryset = TestLink.objects.all()
    serializer_class = TestLinkSerializer