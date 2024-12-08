from .views import *
from django.urls import path, include, re_path


urlpatterns = [
    path('questions/', QuestionAPIList.as_view(), name='question-list'),
    path('answers/', AnswerAPIList.as_view(), name = 'answer-list'),
    path('user/', UserAPIList.as_view(), name = 'user-list'),
    path('user/<int:pk>/', UserAPIList.as_view(), name = 'user-detail'),
    path('test/', TestAPIList.as_view(), name = 'test-list'),
    path('test/<int:pk>/', TestAPIList.as_view(), name = 'test-detail'),
    path('anonymous-participants/', AnonymousParticipantView.as_view(), name='anonymous-participant'),
    path('authenticated-participants/', AuthenticatedParticipantView.as_view(), name='authenticated-participant'),
    path('participant-answer/', ParticipantAnswerAPIList.as_view(), name = 'participant-answer-list'),
    path('test-results/', TestResultAPIList.as_view(), name = 'test-result-list'),
    path('test-links/', TestLinkAPIList.as_view(), name = 'test-link-list'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]