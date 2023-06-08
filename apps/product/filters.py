from django_filters import FilterSet, NumberFilter

from apps.product.models.basket import Basket
from apps.product.models.product import Product


class ProductFilterSet(FilterSet):
    category = NumberFilter(field_name='category_id', lookup_expr='exact')

    class Meta:
        model = Product
        fields = ('category',)
        # fields = {
        #     'price': ['exact'],
        # }


class BasketFilterSet(FilterSet):
    user_id = NumberFilter(field_name='user_id', lookup_expr='exact', required=True)

    class Meta:
        model = Basket
        fields = ('user_id',)
