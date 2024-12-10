from .views import UserAPIList, AnonymousParticipantView, AuthenticatedParticipantView
from django.urls import path
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('data', GetMethod, basename='data')
# urlpatterns = router.urls

urlpatterns = [
    path('', UserAPIList.as_view(), name = 'user-list'),
    path('<int:pk>/', UserAPIList.as_view(), name = 'user-detail'),
    path('auth-part/', AuthenticatedParticipantView.as_view(), name = 'authenticated-participant'),
    path('anon/', AnonymousParticipantView.as_view(), name = 'anonymous-participant'),

    ]