from django.test import TestCase

from test_management.models import Test
from user.models import User, AnonymousParticipant, AuthenticatedParticipant


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='PASSWORD')
        self.test = Test.objects.create(
            title='Test title',
            description='Test description',
            is_active=True,
            is_anonymous=True,
            default_time_limit=30,
            creator=self.user,
        )
        self.anonymous_participant = AnonymousParticipant.objects.create(test=self.test)
        self.authenticated_participant = AuthenticatedParticipant.objects.create(user=self.user, test=self.test)

    def test_anonymous_participant_creation(self):
        self.assertEqual(self.anonymous_participant.test, self.test)

    def test_authenticated_participant_creation(self):
        self.assertEqual(self.authenticated_participant.user, self.user)
        self.assertEqual(self.authenticated_participant.test, self.test)
