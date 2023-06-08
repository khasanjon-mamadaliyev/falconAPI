from django.core.cache import cache
from rest_framework.generics import DestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.shared.utils.generate_random_number import random_number
from apps.shared.utils.send_email import send_email_code
from apps.user.custom_permission import IsAdmin
from apps.user.models import User
from apps.user.serializers import UserSerializer, UserCreateSerializer


class UserModelViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdmin, IsAuthenticated]


class UserDetailAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated, IsAdmin]


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        code = random_number()
        send_email_code()
        cache.set(email, code, 300)
        print(cache.get(email))
        return super().create(request, *args, **kwargs)
