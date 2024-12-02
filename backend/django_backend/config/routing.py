# Пример routing.py для приложения
from django.urls import re_path
from anonymous_question import MyConsumer

websocket_urlpatterns = [
   re_path(r'ws/some_path/$', MyConsumer.as_asgi()),
]