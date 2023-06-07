from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.product.views.basket_api import BasketListAPIView, BasketDetailAPIView, DetailAPIView
from apps.product.views.views import ProductViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
urlpatterns = [
    path('basket', BasketListAPIView.as_view(), name='basket'),
    # path('basket/<int:pk>', DetailAPIView.as_view()),
    path('basket/<int:pk>', BasketDetailAPIView.as_view()),

    # path('basket/<int:pk>', BasketUpdateAPIView.as_view(), name='update'),
    # path('basket/delete/<int:pk>', BasketDestroyAPIView.as_view(), name='delete'),
    # path('category', CategoryListAPIView.as_view()),
    # path('category/<int:pk>', CategoryRetrieveAPIView.as_view()),
    # path('category-product', ProductCategoryListAPIView.as_view()),
    path('', include(router.urls)),
]
