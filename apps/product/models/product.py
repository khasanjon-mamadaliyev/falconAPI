from django.db.models import Model, CharField, IntegerField, SmallIntegerField, TextField, JSONField, CASCADE, \
    ImageField, ForeignKey

from apps.product.models.category import Category
from apps.shared.models import BaseDate


class Product(BaseDate):
    title = CharField(max_length=300)
    price = IntegerField()
    discount = SmallIntegerField()
    description = TextField()
    specifications = JSONField(default=dict, null=True, blank=True)

    category = ForeignKey(Category, CASCADE, 'products')

    @property
    def discount_price(self):
        return self.price - self.price * self.discount // 100

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class ProductImage(Model):
    image = ImageField(upload_to='images/products')
    product = ForeignKey('Product', CASCADE, 'images')

    def __str__(self):
        return self.product.title
