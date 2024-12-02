from django.utils.timezone import now

from django.test import TestCase
from anonymous_question.models import User, Test, Question, Answer, ParticipantAnswer, TestResult
import pytest

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='PASSWORD')
        self.test = Test.objects.create(
            title='Test title',
            description='Test description',
            сreated_at=now(),
            is_active=True,
            is_anonymous=False,
            creator=self.user,
        )
        self.question = Question.objects.create(
            text='What is 2+2?',
            order=1,
            test=self.test,
        )
        self.answer = Answer.objects.create(
            text='4',
            is_correct=False,
            question=self.question,
        )

    def test_creation(self):
        self.assertEqual(Test.objects.count(), 1)
        self.assertEqual(self.test.title, 'Test title')
        self.assertEqual(self.test.creator, self.user)
        self.assertEqual(self.test.description, 'Test description')
        self.assertEqual(self.test.is_active, True)

    def test_question_creation(self):
        self.assertEqual(self.question.text, 'What is 2+2?')
        self.assertEqual(self.question.order, 1)
        self.assertEqual(self.question.test, self.test)

    def test_answer_creation(self):
        self.assertEqual(self.answer.text, '4')
        self.assertEqual(self.answer.is_correct, False)
        self.assertEqual(self.answer.question, self.question)

    def test_participants_answer_creation(self):
        participant_answer = ParticipantAnswer.objects.create(
            selected_option=self.answer,
            participant=self.user,
            question=self.question,
        )
        self.assertEqual(participant_answer.selected_option, self.answer)
        self.assertEqual(participant_answer.participant, self.user)
        self.assertEqual(participant_answer.question, self.question)

    def test_test_result_creation(self):
        test_result = TestResult.objects.create(
            correct_answers=1,
            total_questions=10,
            test=self.test,
            participant=self.user,
        )
        self.assertEqual(test_result.correct_answers, 1)
        self.assertEqual(test_result.total_questions, 10)
        self.assertEqual(test_result.test, self.test)




