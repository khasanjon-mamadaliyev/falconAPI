from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.product.filters import BasketFilterSet
from apps.product.models.basket import Basket
from apps.product.serializers import BasketSerializer


class BasketListAPIView(ListAPIView, ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BasketFilterSet


class BasketDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    http_method_names = ["put", "patch", "delete"]
