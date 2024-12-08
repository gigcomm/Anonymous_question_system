from django.urls import path, include
from rest_framework.routers import DefaultRouter

from test_result.views import TestResultAPIList

urlpatterns = [
    path('', TestResultAPIList.as_view(), name='test-result-list'),
    path('answer/', TestResultAPIList.as_view(), name='participant-answer-list'),

    ]