from django.contrib import admin

from apps.product.models.basket import Basket
from apps.product.models.category import Category
from apps.product.models.like import Like
from apps.product.models.product import Product, ProductImage


class ProductImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline,)


@admin.register(Category)
class ProductModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):
    pass
