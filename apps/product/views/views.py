from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from apps.product.filters import ProductFilterSet
from apps.product.models.category import Category
from apps.product.models.product import Product
from apps.product.serializers import ProductListSerializer, CategoryListSerializer, CategoryRetrieveSerializer, \
    ProductCategorySerializer
from apps.product.services.pagination import CustomPagination


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategoryListSerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategoryRetrieveSerializer


class ProductCategoryListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilterSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPagination
