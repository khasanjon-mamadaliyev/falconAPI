from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

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
