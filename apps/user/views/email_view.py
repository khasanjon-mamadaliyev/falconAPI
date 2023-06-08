from django.core.cache import cache
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from apps.shared.celery_tasks.send_email import send_email_code
from apps.shared.utils.generate_random_number import random_number
from apps.user.models import User
from apps.user.serializers import ActivateEmailSerializer, AgainSendCodeSerializer
from apps.user.services.email_service import email_again_send_code, user_activate_email


class UserActivateEmailAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ActivateEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = user_activate_email(serializer.data)
        return response


class AgainSendCodeEmailAPI(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = AgainSendCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = email_again_send_code(serializer)
        return response
