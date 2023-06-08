from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user.views import UserModelViewSet, UserDetailAPIView, UserListAPIView, UserCreateAPIView

router = DefaultRouter()
router.register('user', UserModelViewSet, basename='user')
urlpatterns = [
    # path('', include(router.urls)),
    path('user/<int:pk>', UserDetailAPIView.as_view(), name='user'),
    path('users', UserListAPIView.as_view(), name='users'),
    path('user', UserCreateAPIView.as_view(), name='user'),
]
