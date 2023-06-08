from django.core.cache import cache

from apps.shared.celery_tasks.send_email import send_email_code
from apps.shared.utils.generate_random_number import random_number


def user_create(email: str):
    code = random_number()
    send_email_code.delay(email, code)
    cache.set(email, code, 300)
    print(cache.get(email))
