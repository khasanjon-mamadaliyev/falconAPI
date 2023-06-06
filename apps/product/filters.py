from django_filters import FilterSet, NumberFilter

from apps.product.models.product import Product


class ProductFilter(FilterSet):
    category = NumberFilter(field_name='category_id', lookup_expr='exact')

    class Meta:
        model = Product
        fields = {
            'price': ['exact'],
        }
