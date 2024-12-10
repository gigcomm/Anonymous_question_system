from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
from django.urls import reverse

from django.utils.timezone import now

from test_link.models import TestLink
from test_management.models import Test
from user.models import User


class TestLinkApiAdvancedTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="PASSWORD")
        self.active_test = Test.objects.create(
            title="Active Test",
            description="Active Test Description",
            сreated_at=now(),
            is_active=True,
            creator=self.user,
        )
        self.inactive_test = Test.objects.create(
            title="Inactive Test",
            description="Inactive Test Description",
            сreated_at=now(),
            is_active=False,
            creator=self.user,
        )
        self.test_link = TestLink.objects.create(test=self.active_test)

    def test_create_test_link_for_inactive_test(self):
        response = self.client.post(
            reverse("test-link-list"),
            data={"test": self.inactive_test.id},
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data,
            {"test": [ErrorDetail(string="Не удается создать ссылку для неактивного теста", code="invalid")]}
        )

    def test_create_duplicate_test_link(self):
        #Попытка создать еще одну ссылку для одного и того же активного теста
        response = self.client.post(
            reverse("test-link-list"),
            data={"test": self.active_test.id},
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(TestLink.objects.filter(test=self.active_test).count(), 2)


    def test_list_links_filter_by_test(self):
        # Создаем несколько ссылок для одного и того же теста
        TestLink.objects.create(test=self.active_test)
        response = self.client.get(reverse("test-link-list") + f"?test={self.active_test.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
