from django.urls import path, include
from rest_framework.routers import DefaultRouter

from test_management.views import *

urlpatterns = [
    path('', TestAPIList.as_view(), name='test-list'),
    path('testdu/<int:pk>/', TestDelUpdView.as_view(), name='test-del-upd'),
    #path('<int:pk>/', TestAPIList.as_view(), name='test-detail'),
    path('questions/', QuestionAPIList.as_view(), name='question-list'),
    path('quedu/<int:pk>/', TestDelUpdView.as_view(), name='question-del-upd'),
    path('answers/', AnswerAPIList.as_view(), name = 'answer-list'),
    path('ansdu/<int:pk>/', TestDelUpdView.as_view(), name='answer-del-upd'),
    path('complete_test/<int:test_id>/', complete_test, name='complete_test'), # Для POST-запроса на завершение теста, чтобы в дальнейшем вызвать celery task
    ]