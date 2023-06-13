# import pytest
# from rest_framework import status
# from rest_framework.reverse import reverse_lazy
# from rest_framework.test import APIClient
#
# from apps.product.models.basket import Basket
# from apps.product.models.category import Category
# from apps.product.models.product import Product
# from apps.user.models import User
#
#
# @pytest.fixture(scope="module")
# def api_client():
#     return APIClient()
#
#
# @pytest.fixture
# def add_category():
#     category = Category.objects.create(name='name')
#     return category
#
#
# @pytest.fixture
# def add_user():
#     user = User.objects.create(first_name='first_name', last_name='last_name', email='email@gmail.com',
#                                phone='900169724', heading='heading', intro='intro')
#     return user
#
#
# @pytest.fixture
# def add_product():
#     product = Product.objects.create(title='title', price=100, discount=10, description='description',
#                                      specifications={"salom": "salom"})
#     return product
#
#
# @pytest.fixture
# def add_basket(add_product, add_user):
#     basket = Basket.objects.create(quantity=12, user_id=add_user.id, product_id=add_product.id)
#     return basket
#
#
# @pytest.mark.django_db
# def test_create_basket(api_client, add_product, add_user):
#     data = {
#         'quantity': 12,
#         'user_id': add_user.id,
#         'product_id': add_product.id
#     }
#     url = reverse_lazy('basket')
#     response = api_client.post(url, data)
#     assert response.status_code == status.HTTP_201_CREATED
#     basket = Basket.objects.first()
#     assert basket is not None
#     assert basket.quantity == data['quantity']
#     assert basket.user_id == data[add_user.id]
#     assert basket.product_id == data[add_product.id]
