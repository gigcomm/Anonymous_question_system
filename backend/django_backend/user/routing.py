# Пример routing.py для приложения
from django.urls import re_path
from user.consumers import WSConsumer

websocket_urlpatterns = [
   re_path(r'ws/some_path/$', WSConsumer.as_asgi()),
]