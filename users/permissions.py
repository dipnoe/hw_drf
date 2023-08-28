from rest_framework.permissions import BasePermission

from users.models import UserRole


class IsModerator(BasePermission):
    """
    Checking if the user is a moderator.
    """
    def has_permission(self, request, view):
        return request.user.role == UserRole.MODERATOR


class IsOwner(BasePermission):
    """
    Checking if the user is the object's owner.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
