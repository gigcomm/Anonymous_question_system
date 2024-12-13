from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('data', GetMethod, basename='data')
# urlpatterns = router.urls

urlpatterns = [
    path('', UserAPIList.as_view(), name = 'user-list'),
    path('<int:pk>/', UserDelUpdView.as_view(), name = 'user-detail'),
    path('auth-part/', AuthenticatedParticipantView.as_view(), name = 'authenticated-participant'),
    path('auth-part/<int:pk>/', AuthParticDelUpdView.as_view(), name = 'auth-partic-del-upd'),
    path('anon/', AnonymousParticipantView.as_view(), name = 'anonymous-participant'),
    path('anon/<int:pk>/', AnonParicDelUpdView.as_view(), name = 'anon-partic-del-upd'),

    ]