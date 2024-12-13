from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework import status, viewsets, generics

from user.serializers import UserSerializer, AnonymousParticipantSerializer, AuthenticatedParticipantSerializer
from user.models import User, AnonymousParticipant, AuthenticatedParticipant

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserView(View):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk=None):
        if pk:
            obj = get_object_or_404(User, pk=pk)
            return JsonResponse({'id': obj.id, 'username': obj.username, 'last_login': obj.last_login})
        else: 
            objects = User.objects.all()
            data = [{'id': obj.id, 'username': obj.username, 'last_login': obj.last_login} for obj in objects]
            return JsonResponse(data, safe=False)
        
    def post(self, request):
        data = request.POST
        new_object = User.objects.create(name=data['name'])
        return JsonResponse({'id': new_object.id, 'username': new_object.username}, status=201)

    def put(self, request, pk):
        data = request.PUT
        obj = get_object_or_404(User, pk=pk)
        obj.name = data['username']
        obj.save()
        return JsonResponse({'id': obj.id, 'username': obj.username})

    def delete(self, request, pk):
        obj = get_object_or_404(User, pk=pk)
        obj.delete()
        return JsonResponse({'message': 'Deleted successfully'})

class AnonymousParticipantView(generics.ListCreateAPIView):
    queryset = AnonymousParticipant.objects.all()
    serializer_class = AnonymousParticipantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AnonParicDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnonymousParticipant.objects.all()
    serializer_class = AnonymousParticipantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthenticatedParticipantView(generics.ListCreateAPIView):
    queryset = AuthenticatedParticipant.objects.all()
    serializer_class = AuthenticatedParticipantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthParticDelUpdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthenticatedParticipant.objects.all()
    serializer_class = AuthenticatedParticipantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]