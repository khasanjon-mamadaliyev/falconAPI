from .celery import app as celery_app
import apps  # noqa

__all__ = ['celery_app']
