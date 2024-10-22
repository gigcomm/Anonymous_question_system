from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', GetMethod, basename='data')
urlpatterns = router.urls