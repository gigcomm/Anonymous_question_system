import uuid

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from test_management.models import Test, Question, Answer
from user.models import AnonymousParticipant, AuthenticatedParticipant, User
from test_result.models import TestResult, ParticipantAnswer



class TestResultApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="PASSWORD")
        self.test = Test.objects.create(
            title="Sample Test",
            description="Sample Test Description",
            is_active=True,
            creator=self.user,
        )
        self.anonymous_participant = AnonymousParticipant.objects.create(identifier=uuid.uuid4(), test=self.test)
        self.authenticated_participant = AuthenticatedParticipant.objects.create(user=self.user, test=self.test)

        self.question = Question.objects.create(test=self.test, text="What is the capital of France?", order="1")
        self.answer = Answer.objects.create(question=self.question, text="Paris")

        self.test_result = TestResult.objects.create(
            test=self.test,
            anonymous_participant=self.anonymous_participant,
            correct_answers=1,
            total_questions=1,
        )

    def test_create_test_result(self):
        # Создаем результат теста для анонимного участника
        response = self.client.post(reverse("test-result-list"), data={
            "test": self.test.id,
            "anonymous_participant": self.anonymous_participant.id,
            "correct_answers": 1,
            "total_questions": 1,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TestResult.objects.count(), 2)

    def test_create_test_result_for_authenticated_participant(self):
        # Создаем результат теста для аутентифицированного участника
        response = self.client.post(reverse("test-result-list"), data={
            "test": self.test.id,
            "authenticated_participant": self.authenticated_participant.id,
            "correct_answers": 1,
            "total_questions": 1,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TestResult.objects.count(), 2)

    def test_list_test_results(self):
        # Список результатов тестов
        response = self.client.get(reverse("test-result-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_results_by_participant_type(self):
        # Фильтрация результатов тестов по типу участника
        response = self.client.get(
            reverse("test-result-list") + f"?anonymous_participant={self.anonymous_participant.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            reverse("test-result-list") + f"?authenticated_participant={self.authenticated_participant.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # def test_create_participant_answer(self):
    #     # Подготовка данных для создания ответа участника
    #     participant_answer_data = {
    #         "selected_option": self.answer.id,
    #         "question": self.question.id,
    #         "anonymous_participant": self.anonymous_participant.id,
    #         "test": self.test.id,
    #     }
    #     response = self.client.post(reverse("participant-answer-list"), data=participant_answer_data)
    #
    #     if response.status_code != status.HTTP_201_CREATED:
    #         print("Response Data:", response.data)  # Логи ошибок
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(ParticipantAnswer.objects.count(), 1)
    #
    #     # Для аутентифицированного участника
    #     participant_answer_data["anonymous_participant"] = None
    #     participant_answer_data["authenticated_participant"] = self.authenticated_participant.id
    #     response = self.client.post(reverse("participant-answer-list"), data=participant_answer_data)
    #
    #     if response.status_code != status.HTTP_201_CREATED:
    #         print("Response Data:", response.data)
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(ParticipantAnswer.objects.count(), 2)

    def test_list_participant_answers(self):
        # Список ответов участников
        response = self.client.get(reverse("participant-answer-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_answers_by_participant_type(self):
        # Создаем ответы для анонимного и аутентифицированного участника
        ParticipantAnswer.objects.create(selected_option=self.answer, question=self.question,
                                         anonymous_participant=self.anonymous_participant)
        ParticipantAnswer.objects.create(selected_option=self.answer, question=self.question,
                                         authenticated_participant=self.authenticated_participant)

        # Проверяем фильтрацию по анонимному участнику
        response = self.client.get(
            reverse("participant-answer-list") + f"?anonymous_participant={self.anonymous_participant.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Проверяем фильтрацию по аутентифицированному участнику
        response = self.client.get(
            reverse("participant-answer-list") + f"?authenticated_participant={self.authenticated_participant.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ожидается 1 ответ для аутентифицированного участника
