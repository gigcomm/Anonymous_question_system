from django.utils.timezone import now

from django.test import TestCase
from anonymous_question.models import User, Test, Question, Answer, ParticipantAnswer, TestResult, AnonymousParticipant, \
    AuthenticatedParticipant


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='PASSWORD')
        self.test = Test.objects.create(
            title='Test title',
            description='Test description',
            сreated_at=now(),
            is_active=True,
            is_anonymous=True,
            default_time_limit=30,
            creator=self.user,
        )
        self.question = Question.objects.create(
            text='What is 2+2?',
            order=1,
            test=self.test,
        )
        self.answer = Answer.objects.create(
            text='4',
            is_correct=True,
            question=self.question,
        )
        self.anonymous_participant = AnonymousParticipant.objects.create(test=self.test)
        self.authenticated_participant = AuthenticatedParticipant.objects.create(user=self.user, test=self.test)

    def test_creation(self):
        self.assertEqual(Test.objects.count(), 1)
        self.assertEqual(self.test.title, 'Test title')
        self.assertEqual(self.test.creator, self.user)
        self.assertEqual(self.test.description, 'Test description')
        self.assertEqual(self.test.is_active, True)
        self.assertEqual(self.test.is_anonymous, True)
        self.assertEqual(self.test.default_time_limit, 30)

    def test_anonymous_participant_creation(self):
        self.assertEqual(self.anonymous_participant.test, self.test)

    def test_authenticated_participant_creation(self):
        self.assertEqual(self.authenticated_participant.user, self.user)
        self.assertEqual(self.authenticated_participant.test, self.test)

    def test_question_creation(self):
        self.assertEqual(self.question.text, 'What is 2+2?')
        self.assertEqual(self.question.order, 1)
        self.assertEqual(self.question.test, self.test)

    def test_answer_creation(self):
        self.assertEqual(self.answer.text, '4')
        self.assertEqual(self.answer.is_correct, True)
        self.assertEqual(self.answer.question, self.question)

    def test_participants_answer_creation(self):
        participant_answer = ParticipantAnswer.objects.create(
            selected_option=self.answer,
            anonymous_participant=self.anonymous_participant,
            question=self.question,
        )
        self.assertEqual(participant_answer.selected_option, self.answer)
        self.assertEqual(participant_answer.anonymous_participant, self.anonymous_participant)
        self.assertEqual(participant_answer.question, self.question)

    def test_test_result_creation_for_anonymous_participant(self):
        test_result = TestResult.objects.create(
            correct_answers=1,
            total_questions=10,
            test=self.test,
            anonymous_participant=self.anonymous_participant,
        )
        self.assertEqual(test_result.correct_answers, 1)
        self.assertEqual(test_result.total_questions, 10)
        self.assertEqual(test_result.test, self.test)
        self.assertEqual(test_result.anonymous_participant, self.anonymous_participant)

    def test_test_result_creation_for_authenticated_participant(self):
        test_result = TestResult.objects.create(
            correct_answers=5,
            total_questions=10,
            test=self.test,
            authenticated_participant=self.authenticated_participant,
        )
        self.assertEqual(test_result.correct_answers, 5)
        self.assertEqual(test_result.total_questions, 10)
        self.assertEqual(test_result.test, self.test)
        self.assertEqual(test_result.authenticated_participant, self.authenticated_participant)
