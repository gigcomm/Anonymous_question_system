from rest_framework import serializers
from user.models  import User, AnonymousParticipant, AuthenticatedParticipant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        ref_name = "CustomUserSerializer"


class AnonymousParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousParticipant
        fields = '__all__'


class AuthenticatedParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticatedParticipant
        fields = '__all__'