from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views import ProductListAPIView, ProductDetailAPIView, BasketCreateAPIView, BasketUpdateAPIView, \
    CategoryListAPIView, CategoryRetrieveAPIView, ProductCategoryListAPIView, ProductViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
    # path('', ProductListAPIView.as_view(), name='products'),
    # path('detail/<int:pk>', ProductDetailAPIView.as_view(), name='detail'),
    # path('create', BasketCreateAPIView.as_view(), name='create'),
    # path('basket/<int:pk>', BasketUpdateAPIView.as_view(), name='update'),
    # path('category', CategoryListAPIView.as_view()),
    # path('category/<int:pk>', CategoryRetrieveAPIView.as_view()),
    # path('category-product', ProductCategoryListAPIView.as_view()),
    path('', include(router.urls))
]
