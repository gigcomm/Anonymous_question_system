from django.test import TestCase

from django.utils.timezone import now
from rest_framework.exceptions import ValidationError

from test_link.models import TestLink
from test_link.serializers import TestLinkSerializer
from test_management.models import Test
from user.models import User


class TestLinkSerializerAdvancedTestCase(TestCase):
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

    def test_serializer_valid_data(self):
        serializer = TestLinkSerializer(
            data={"test": self.active_test.id}
        )
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data_inactive_test(self):
        serializer = TestLinkSerializer(
            data={"test": self.inactive_test.id}
        )
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_serializer_auto_generated_fields(self):
        test_link = TestLink.objects.create(test=self.active_test)
        serializer = TestLinkSerializer(instance=test_link)
        self.assertEqual(serializer.data["test"], self.active_test.id)
        self.assertTrue("created_at" in serializer.data)
        self.assertTrue("link" in serializer.data)
