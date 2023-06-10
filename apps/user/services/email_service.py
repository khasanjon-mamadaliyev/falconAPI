from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from apps.shared.celery_tasks.send_email import send_email_code
from apps.shared.utils.generate_random_number import random_number
from apps.user.models import User


def email_again_send_code(serializer):
    email = serializer.data.get('email')
    user = get_object_or_404(User, email=email)
    if user.is_active:
        raise ValidationError('Email already activated !')
    code = random_number()
    send_email_code.delay(email, code)
    cache.set(email, code, 300)
    print(cache.get(email))
    return Response('Verification code has been sent to your email !', status.HTTP_200_OK)


def user_activate_email(data):
    email = data.get('email')
    confirm_code = data.get('code')
    code = cache.get(email)
    user = get_object_or_404(User, email=email)
    if not user.is_active:
        if code:
            if code == confirm_code:
                User.objects.filter(email=email).update(is_active=True)
                cache.delete(email)
                return Response('Successfully activated your email !', status.HTTP_200_OK)
            return Response('Verify code is not correct', status.HTTP_404_NOT_FOUND)
        return Response('Your verification code is expired !', status.HTTP_404_NOT_FOUND)
    raise ValidationError('Email already activated !')
