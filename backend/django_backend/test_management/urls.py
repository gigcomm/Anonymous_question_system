from django.urls import path, include
from rest_framework.routers import DefaultRouter

from test_management.views import TestAPIList, AnswerAPIList, QuestionAPIList

urlpatterns = [
    path('', TestAPIList.as_view(), name='test-list'),
    #path('<int:pk>/', TestAPIList.as_view(), name='test-detail'),
    path('questions/', QuestionAPIList.as_view(), name='question-list'),
    path('answers/', AnswerAPIList.as_view(), name = 'answer-list'),
    
    ]