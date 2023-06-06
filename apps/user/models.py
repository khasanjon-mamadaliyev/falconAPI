from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import CharField, BooleanField, EmailField, ImageField, TextField

from apps.shared.models import BaseDate, CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, BaseDate):
    image = ImageField(upload_to='images/users', null=True, blank=True)
    first_name = CharField('first name', max_length=150)
    last_name = CharField('last name', max_length=150, null=True, blank=True)
    email = EmailField(max_length=250, unique=True)
    phone = CharField(max_length=15, unique=True, null=True, blank=True)
    is_staff = BooleanField('staff status', default=False)
    is_active = BooleanField('active', default=False)
    heading = CharField(max_length=200)
    intro = TextField(null=True, blank=True)

    objects = CustomUserManager()
    PHONE_FIELD = 'email'
    USERNAME_FIELD = 'email'

    @property
    def my_basket(self):
        return self.basket_set.all()
