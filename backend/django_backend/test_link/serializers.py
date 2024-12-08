from rest_framework import serializers
from test_link.models import TestLink

class TestLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestLink
        fields = '__all__'