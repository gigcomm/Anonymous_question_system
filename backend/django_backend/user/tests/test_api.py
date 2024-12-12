import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User, AnonymousParticipant, AuthenticatedParticipant
from test_management.models import Test

@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="password")


# Fixture для создания теста
@pytest.fixture
def test_obj(user):
    return Test.objects.create(title="Sample Test", creator=user)


# Fixture для создания анонимного участника
@pytest.fixture
def anonymous_participant(test_obj):
    return AnonymousParticipant.objects.create(test=test_obj)


# Fixture для создания аутентифицированного участника
@pytest.fixture
def authenticated_participant(user, test_obj):
    return AuthenticatedParticipant.objects.create(user=user, test=test_obj)


# Тест для создания пользователя через API
@pytest.mark.django_db
def test_user_creation_api():
    client = APIClient()
    url = reverse('user-list')
    data = {'username': 'newuser', 'password': 'testpassword', 'email': 'testemail@testemail.com'}

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username='newuser').exists()


# Тест для создания анонимного участника через API
@pytest.mark.django_db
def test_anonymous_participant_creation_api(test_obj):
    client = APIClient()
    url = reverse('anonymous-participant')  # Убедитесь, что у вас есть маршрут, связанный с этой целью

    data = {'test': test_obj.id}
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert AnonymousParticipant.objects.filter(test=test_obj).exists()


# Тест для создания аутентифицированного участника через API
@pytest.mark.django_db
def test_authenticated_participant_creation_api(user, test_obj):
    client = APIClient()
    url = reverse('authenticated-participant')  # Убедитесь, что у вас есть маршрут, связанный с этой целью

    data = {'user': user.id, 'test': test_obj.id}
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert AuthenticatedParticipant.objects.filter(user=user, test=test_obj).exists()
