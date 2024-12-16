from django.urls import path, include
from rest_framework.routers import DefaultRouter

from test_result.views import *

urlpatterns = [
    path('', TestResultAPIList.as_view(), name='test-result-list'),
    path('answer/', ParticipantAnswerAPIList.as_view(), name='participant-answer-list'),
    path('answer/<int:pk>/', ParticAnswerDelUpdView.as_view(), name='participant-answer-del-upd'),
    path('<int:pk>/', ParticAnswerDelUpdView.as_view(), name='participant-answer-del-upd'),

    ]