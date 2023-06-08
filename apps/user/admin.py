from django.contrib import admin

from apps.user.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass
