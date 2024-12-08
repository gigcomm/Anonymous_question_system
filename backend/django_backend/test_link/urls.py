from django.urls import path, include
from rest_framework.routers import DefaultRouter

from test_link.views import TestLinkAPIList

urlpatterns = [
    path('test-links/', TestLinkAPIList.as_view(), name='test-link-list'),
    ]