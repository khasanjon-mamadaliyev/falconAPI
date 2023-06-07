from rest_framework.serializers import ModelSerializer

from apps.product.models.basket import Basket
from apps.product.models.category import Category
from apps.product.models.product import Product


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        data = CategoryListSerializer(instance.children.all(), many=True).data
        represent['children'] = data if data else None
        return represent


class CategoryRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        data = CategoryRetrieveSerializer(instance.children.all(), many=True).data
        represent['children'] = data if data else None
        return represent


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BasketSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'
