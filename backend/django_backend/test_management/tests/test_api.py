from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from test_management.models import Test, Question, Answer
from django.contrib.auth import get_user_model

User = get_user_model()

class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user")
        self.test = Test.objects.create(title="Sample Test", creator=self.user)
        self.question = Question.objects.create(text="Sample Question", test=self.test, order=1)
        self.answer = Answer.objects.create(text="Sample Answer", question=self.question)
        self.test_url = reverse("test-list")
        self.question_url = reverse("question-list")
        self.answer_url = reverse("answer-list")

    def test_create_test(self):
        data = {"title": "New Test", "creator": self.user.id}
        response = self.client.post(self.test_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Test")

    def test_get_tests(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_question(self):
        data = {"text": "New Question", "test": self.test.id, "order": "1"}
        response = self.client.post(self.question_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["text"], "New Question")

    def test_get_questions(self):
        response = self.client.get(self.question_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_answer(self):
        data = {"text": "New Answer", "question": self.question.id}
        response = self.client.post(self.answer_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["text"], "New Answer")

    def test_get_answers(self):
        response = self.client.get(self.answer_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
