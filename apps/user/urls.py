from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user.views.email_view import UserActivateEmailAPIView, AgainSendCodeEmailAPI
from apps.user.views.user_view import UserModelViewSet, UserDetailAPIView, UserListAPIView, UserCreateAPIView

router = DefaultRouter()
router.register('user', UserModelViewSet, basename='user')
urlpatterns = [
    # path('', include(router.urls)),
    path('user/<int:pk>', UserDetailAPIView.as_view(), name='user'),
    path('users', UserListAPIView.as_view(), name='users'),
    path('user', UserCreateAPIView.as_view(), name='user'),
    path('user-activate', UserActivateEmailAPIView.as_view(), name='user_activate'),
    path('user-again-code', AgainSendCodeEmailAPI.as_view(), name='again_code')
]
