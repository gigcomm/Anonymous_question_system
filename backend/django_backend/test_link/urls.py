from django.urls import path


from test_link.views import *

urlpatterns = [
    path('', TestLinkAPIList.as_view(), name='test-link-list'),
    path('<int:pk>/', TestLinkDelUpdView.as_view(), name='test-link-del-upd'),
    path('<uuid:link>/', TestLinkView.as_view(), name='test-link-view'),
    ]