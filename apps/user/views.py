from django.core.cache import cache
from django.db.models import F
from rest_framework import status
from rest_framework.generics import DestroyAPIView, ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.shared.celery_tasks.send_email import send_email_code
from apps.shared.utils.generate_random_number import random_number
from apps.user.models import User
from apps.user.serializers import UserSerializer, UserCreateSerializer, UserActivateSerializer


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
        send_email_code.delay(email, code, first_name)
        cache.set(email, code, 300)
        print(cache.get(email))
        return super().create(request, *args, **kwargs)


class UserActivateEmailAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserActivateSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = cache.get(email)
        if code:
            confirm_code = request.data.get('code')
            if code == confirm_code:
                User.objects.filter(email=email).update(is_active=True)
                return Response('Successfully activated your email !', status.HTTP_200_OK)
            return Response('Verify code is not correct', status.HTTP_404_NOT_FOUND)
        return Response('Your verification code is expired !', status.HTTP_404_NOT_FOUND)
