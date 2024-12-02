from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('data', GetMethod, basename='data')
# urlpatterns = router.urls

urlpatterns = [
    path('questions/', QuestionAPIList.as_view(), name='question-list'),
    path('answers/', AnswerAPIList.as_view(), name = 'answer-list'),
    path('user/', UserAPIList.as_view(), name = 'user-list'),
    path('test/', TestAPIList.as_view(), name = 'test-list'),
    path('participantAnswer/', ParticipantAnswerAPIList.as_view(), name = 'participantAnswer-list'),
    path('testResult/', TestResultAPIList.as_view(), name = 'testResult-list'),
    path('testLink/', TestLinkAPIList.as_view(), name = 'testLink-list'),
]