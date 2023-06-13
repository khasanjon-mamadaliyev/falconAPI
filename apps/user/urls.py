from django.urls import path

from apps.user.views.email_view import UserActivateEmailAPIView, AgainActivateEmailAPIView
from apps.user.views.user_view import UserRetrieveUpdateDestroyAPIView, UserCreateAPIView

urlpatterns = [
    path('user/register', UserCreateAPIView.as_view(), name='user_post'),
    path('user/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('user/activate', UserActivateEmailAPIView.as_view(), name='user_activate'),
    path('user/again-activate', AgainActivateEmailAPIView.as_view(), name='again_activate'),
]
