FROM python:3.10.6-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /requirements.txt

COPY compose/django-docker/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint



COPY compose/django-docker/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY compose/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker


#COPY compose/celery/beat/start /start-celerybeat
#RUN sed -i 's/\r$//g' /start-celerybeat
#RUN chmod +x /start-celerybeat
COPY compose/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

WORKDIR /app

ENTRYPOINT ["sh", "/entrypoint"]