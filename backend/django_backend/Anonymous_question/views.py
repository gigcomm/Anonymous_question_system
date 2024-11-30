from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from .models import *
from .serializers import*

# Create your views here.

#Представление для получения списка вопросов и создания нового вопроса
class QuestionAPIList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TestAPIList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class AnswerAPIList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class ParticipantAnswerAPIList(generics.ListCreateAPIView):
    queryset = ParticipantAnswer.objects.all()
    serializer_class = ParticipantAnswerSerializer

class TestResultAPIList(generics.ListCreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

class TestLinkAPIList(generics.ListCreateAPIView):
    queryset = TestLink.objects.all()
    serializer_class = TestLinkSerializer

# # Представление для получения, обновления или удаления конкретного вопроса
# class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class GetMethod(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

#     def list(self, request, *args, **kwargs):
#         data = list(Question.objects.all().values())
#         return Response(data)

#     def retrieve(self, request, *args, **kwargs):
#         data = list(Question.objects.filter(id=kwargs['pk']).values())
#         return Response(data)

#     def create(self, request, *args, **kwargs):
#         question_serializer_data = QuestionSerializer(data=request.data)
#         if question_serializer_data.is_valid():
#             question_serializer_data.save()
#             status_code = status.HTTP_201_CREATED
#             return Response({"message": "Product Added Sucessfully", "status": status_code})
#         else:
#             status_code = status.HTTP_400_BAD_REQUEST
#             return Response({"message": "please fill the datails", "status": status_code})

#     def destroy(self, request, *args, **kwargs):
#         question_data = Question.objects.filter(id=kwargs['pk'])
#         if question_data:
#             question_data.delete()
#             status_code = status.HTTP_201_CREATED
#             return Response({"message": "Product delete Sucessfully", "status": status_code})
#         else:
#             status_code = status.HTTP_400_BAD_REQUEST
#             return Response({"message": "Product data not found", "status": status_code})

#     def update(self, request, *args, **kwargs):
#         question_details = Question.objects.get(id=kwargs['pk'])
#         question_serializer_data = QuestionSerializer(
#             question_details, data=request.data, partial=True)
#         if question_serializer_data.is_valid():
#             question_serializer_data.save()
#             status_code = status.HTTP_201_CREATED
#             return Response({"message": "Product Update Sucessfully", "status": status_code})
#         else:
#             status_code = status.HTTP_400_BAD_REQUEST
#             return Response({"message": "Product data Not found", "status": status_code})
