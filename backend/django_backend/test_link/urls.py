from django.urls import path, include
from rest_framework.routers import DefaultRouter

from test_link.views import *

urlpatterns = [
    path('', TestLinkAPIList.as_view(), name='test-link-list'),
    path('<int:pk>/', TestLinkDelUpdView.as_view(), name='test-link-del-upd'),
    ]