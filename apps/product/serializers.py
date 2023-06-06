from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from apps.product.models.basket import Basket
from apps.product.models.category import Category
from apps.product.models.product import Product
from apps.user.models import User


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ('updated_at', 'created_at')


class BasketCreateSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class BasketUpdateSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class BasketListSerializer(ModelSerializer):
    class Meta:
        model = Basket
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
