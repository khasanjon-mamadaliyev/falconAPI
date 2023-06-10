from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from apps.user.models import User
from apps.user.serializers import UserSerializer, UserCreateSerializer
from apps.user.services.user_service import user_create


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_create(serializer.data['email'])
        return super().create(request, *args, **kwargs)
