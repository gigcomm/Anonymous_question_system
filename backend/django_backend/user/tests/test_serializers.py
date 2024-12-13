import pytest
from user.serializers import UserSerializer, AnonymousParticipantSerializer, AuthenticatedParticipantSerializer
from user.models import User
from test_management.models import Test


@pytest.mark.django_db
def test_user_serializer_valid_data():
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'strongpassword123'
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    user = serializer.save()
    assert user.username == data['username']
    assert user.email == data['email']


@pytest.mark.django_db
def test_user_serializer_invalid_data():
    data = {
        'username': '',
        'email': 'invalid-email',
        'password': ''
    }
    serializer = UserSerializer(data=data)
    assert not serializer.is_valid()
    assert 'username' in serializer.errors
    assert 'email' in serializer.errors
    assert 'password' in serializer.errors


@pytest.mark.django_db
def test_anonymous_participant_serializer():
    user = User.objects.create(username='testuser')
    test_instance = Test.objects.create(title='Sample Test', creator=user)
    data = {
        'test': test_instance.id,
    }
    serializer = AnonymousParticipantSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    participant = serializer.save()
    assert participant.test == test_instance


@pytest.mark.django_db
def test_authenticated_participant_serializer():
    user = User.objects.create(username='testuser')
    test_instance = Test.objects.create(title='Sample Test', creator=user)
    data = {
        'user': user.id,
        'test': test_instance.id,
    }
    serializer = AuthenticatedParticipantSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    participant = serializer.save()
    assert participant.user == user
    assert participant.test == test_instance
