# Пример routing.py для приложения
from django.urls import path
from test_management.consumers import TestRoomConsumer

websocket_urlpatterns = [
   path('ws/test/<uuid:test_link>/', TestRoomConsumer.as_asgi()),
]