from django.test import TestCase
from django.utils.timezone import now

from test_management.models import Test, Question, Answer
from user.models import User


class TestQuestionAnswerTestCase(TestCase):
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

    def test_creation(self):
        self.assertEqual(Test.objects.count(), 1)
        self.assertEqual(self.test.title, 'Test title')
        self.assertEqual(self.test.creator, self.user)
        self.assertEqual(self.test.description, 'Test description')
        self.assertEqual(self.test.is_active, True)
        self.assertEqual(self.test.is_anonymous, True)
        self.assertEqual(self.test.default_time_limit, 30)

    def test_question_creation(self):
        self.assertEqual(self.question.text, 'What is 2+2?')
        self.assertEqual(self.question.order, 1)
        self.assertEqual(self.question.test, self.test)

    def test_answer_creation(self):
        self.assertEqual(self.answer.text, '4')
        self.assertEqual(self.answer.is_correct, True)
        self.assertEqual(self.answer.question, self.question)
