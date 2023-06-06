from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from apps.product.filters import ProductFilter
from apps.product.models.basket import Basket
from apps.product.models.category import Category
from apps.product.models.product import Product
from apps.product.serializers import ProductListSerializer, ProductDetailSerializer, BasketCreateSerializer, \
    BasketUpdateSerializer, CategoryListSerializer, CategoryRetrieveSerializer, \
    ProductCategorySerializer
from apps.product.services.pagination import CustomPagination


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPagination


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class BasketCreateAPIView(CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketCreateSerializer


class BasketUpdateAPIView(UpdateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketUpdateSerializer


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
    filterset_class = ProductFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPagination
