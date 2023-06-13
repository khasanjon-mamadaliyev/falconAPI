# import pytest
# from rest_framework import status
# from rest_framework.reverse import reverse_lazy
# from rest_framework.test import APIClient
#
# from apps.user.models import User
#
# client = APIClient()
#
#
# @pytest.mark.django_db
# def test_create_user():
#     url = reverse_lazy('user_post')
#     data = {
#         'first_name': 'first_name',
#         'last_name': 'last_name',
#         'email': 'email@gmail.com',
#         'phone': '900169724',
#         'heading': 'heading',
#         'intro': 'intro'
#     }
#     # ('first_name', 'last_name', 'email', 'heading', 'password')
#     response = client.post(url, data)
#
#     assert response.status_code == status.HTTP_201_CREATED
#     user = User.objects.first()
#     assert user is not None
#     assert response.json() == data
