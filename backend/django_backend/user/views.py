from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics

from user.serializers import UserSerializer, AnonymousParticipantSerializer, AuthenticatedParticipantSerializer
from user.models import User, AnonymousParticipant, AuthenticatedParticipant


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnonymousParticipantView(generics.ListCreateAPIView):
    queryset = AnonymousParticipant.objects.all()
    serializer_class = AnonymousParticipantSerializer


class AuthenticatedParticipantView(generics.ListCreateAPIView):
    queryset = AuthenticatedParticipant.objects.all()
    serializer_class = AuthenticatedParticipantSerializer