from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField, EmailField
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer, Serializer

from apps.user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(ModelSerializer):
    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return super().validate(attrs)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'heading', 'password')


class ActivateEmailSerializer(Serializer):
    code = IntegerField()
    email = EmailField()


class AgainSendCodeSerializer(Serializer):
    email = EmailField()
