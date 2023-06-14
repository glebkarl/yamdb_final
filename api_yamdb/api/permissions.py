from rest_framework import permissions
from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAuthenticatedOrReadOnly)


class AuthorOrModeratorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
            or request.user.moderator()
        )


class AdminOrSuperuser(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.admin() or request.user.is_superuser)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and (request.user.admin() or request.user.is_superuser)
        )


class TitlePermission(permissions.BasePermission):

    message = 'Вы не имеете таких полномочий.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.role == 'admin' or request.user.is_superuser:
            return True
        return False


class RewiewsPermission(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
            or request.user.moderator()
            or request.user.admin()
        )
