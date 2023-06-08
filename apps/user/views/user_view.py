from django.core.cache import cache
from rest_framework.generics import DestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.shared.celery_tasks.send_email import send_email_code
from apps.shared.utils.generate_random_number import random_number
from apps.user.models import User
from apps.user.serializers import UserSerializer, UserCreateSerializer
from apps.user.services.user_service import user_create


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
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_create(serializer.data['email'])
        return super().create(request, *args, **kwargs)
