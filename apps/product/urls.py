from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views.basket_api import BasketListAPIView, BasketDetailAPIView
from apps.product.views.product_api import ProductViewSet, CategoryListAPIView

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
urlpatterns = [
    path('basket', BasketListAPIView.as_view(), name='basket'),
    path('basket/<int:pk>', BasketDetailAPIView.as_view(), name='basket'),
    path('category', CategoryListAPIView.as_view()),
    # path('category/<int:pk>', CategoryRetrieveAPIView.as_view()),
    # path('category-product', ProductCategoryListAPIView.as_view()),
    path('', include(router.urls)),
]
