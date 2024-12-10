import uuid

from django.test import TestCase
from test_result.models import TestResult, ParticipantAnswer, Test
from test_result.serializers import TestResultSerializer, ParticipantAnswerSerializer
from user.models import AnonymousParticipant, AuthenticatedParticipant, User
from test_management.models import Answer, Question

class TestResultSerializers(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.test = Test.objects.create(title="Sample Test", creator=self.user)
        self.anonymous_participant = AnonymousParticipant.objects.create(identifier=uuid.uuid4(), test=self.test)
        self.authenticated_participant = AuthenticatedParticipant.objects.create(user=self.user, test=self.test)
        self.test_result = TestResult.objects.create(
            correct_answers=5,
            total_questions=10,
            test=self.test,
            anonymous_participant=self.anonymous_participant
        )

    def test_test_result_serializer(self):
        serializer = TestResultSerializer(self.test_result)
        data = serializer.data
        self.assertEqual(data['correct_answers'], 5)
        self.assertEqual(data['total_questions'], 10)
        self.assertEqual(data['test'], self.test.id)
        self.assertEqual(data['anonymous_participant'], self.anonymous_participant.id)

class ParticipantAnswerSerializers(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.test = Test.objects.create(title="Sample Test", creator=self.user)
        self.anonymous_participant = AnonymousParticipant.objects.create(identifier=uuid.uuid4(), test=self.test)
        self.authenticated_participant = AuthenticatedParticipant.objects.create(user=self.user, test=self.test)
        self.question = Question.objects.create(text="Sample Question", order=1, test=self.test)
        self.answer = Answer.objects.create(text="Sample Answer", is_correct=True, question=self.question)
        self.participant_answer = ParticipantAnswer.objects.create(
            selected_option=self.answer,
            question=self.question,
            anonymous_participant=self.anonymous_participant
        )

    def test_participant_answer_serializer(self):
        serializer = ParticipantAnswerSerializer(self.participant_answer)
        data = serializer.data
        self.assertEqual(data['selected_option'], self.answer.id)
        self.assertEqual(data['question'], self.question.id)
        self.assertEqual(data['anonymous_participant'], self.anonymous_participant.id)
