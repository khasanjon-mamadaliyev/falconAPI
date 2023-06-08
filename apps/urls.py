from django.urls import path, include

urlpatterns = [
    path('', include('apps.product.urls')),
    path('', include('apps.user.urls'))
]
