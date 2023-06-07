from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import UpdateAPIView, ListAPIView, DestroyAPIView, ListCreateAPIView, \
    GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from apps.product.filters import BasketFilterSet
from apps.product.models.basket import Basket
from apps.product.serializers import BasketSerializer


class BasketListAPIView(ListAPIView, ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BasketFilterSet


class BasketUpdateAPIView(UpdateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketDestroyAPIView(DestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketDetailAPIView(UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class DetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
