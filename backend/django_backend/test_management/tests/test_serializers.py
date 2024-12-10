from django.test import TestCase
from .models import Test, Question, Answer
from .serializers import TestSerializer, QuestionSerializer, AnswerSerializer

class TestSerializers(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.test = Test.objects.create(title="Sample Test", description="Description", creator=self.user)
        self.question = Question.objects.create(text="Sample Question", order=1, test=self.test)
        self.answer = Answer.objects.create(text="Sample Answer", is_correct=True, question=self.question)

    def test_test_serializer(self):
        serializer = TestSerializer(self.test)
        data = serializer.data
        self.assertEqual(data['title'], "Sample Test")
        self.assertEqual(data['creator'], self.test.creator.id)

    def test_question_serializer(self):
        serializer = QuestionSerializer(self.question)
        data = serializer.data
        self.assertEqual(data['text'], "Sample Question")
        self.assertEqual(data['test'], self.test.id)

    def test_answer_serializer(self):
        serializer = AnswerSerializer(self.answer)
        data = serializer.data
        self.assertEqual(data['text'], "Sample Answer")
        self.assertEqual(data['question'], self.question.id)
