from django.db.models import Model, ForeignKey, CASCADE

from apps.product.models.product import Product
from apps.user.models import User


class Like(Model):
    user = ForeignKey(User, CASCADE)
    product = ForeignKey(Product, CASCADE)

    class Meta:
        unique_together = ('user', 'product')
