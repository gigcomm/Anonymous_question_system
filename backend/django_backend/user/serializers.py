from rest_framework import serializers
from user.models  import User, AnonymousParticipant, AuthenticatedParticipant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        ref_name = "CustomUserSerializer"

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Некорректный email")
        return value

    def validate_username(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Имя пользователя должно содержать как минимум 3 символа")
        return value

class AnonymousParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousParticipant
        fields = '__all__'

    def validate(self, attrs):
        if not attrs.get('test'):
            raise serializers.ValidationError("Участник должен быть связан с тестом")
        return attrs

class AuthenticatedParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticatedParticipant
        fields = '__all__'

    def validate(self, attrs):
        if not attrs.get('user'):
            raise serializers.ValidationError("Участник должен быть связан с пользователем")
        if not attrs.get('test'):
            raise serializers.ValidationError("Участник должен быть связан с тестом")
        return attrs