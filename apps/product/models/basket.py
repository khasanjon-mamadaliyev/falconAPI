from django.db.models import Model, IntegerField, ForeignKey, CASCADE

from apps.product.models.product import Product
from apps.user.models import User


class Basket(Model):
    quantity = IntegerField()
    user = ForeignKey(User, CASCADE)
    product = ForeignKey(Product, CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return self.product.title
