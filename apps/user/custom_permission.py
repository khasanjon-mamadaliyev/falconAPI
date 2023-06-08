from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    # def has_permission(self, request, view):
    #     return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_superuser
