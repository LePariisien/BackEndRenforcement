from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission qui permet de modifier un objet uniquement si l'utilisateur en est le propriétaire.
    """

    def has_object_permission(self, request, view, obj):
        # Autoriser la lecture (GET, HEAD, OPTIONS) à tous
        if request.method in permissions.SAFE_METHODS:
            return True

        # Sinon, vérifier que l'utilisateur est le propriétaire de l'objet
        return obj.utilisateur == request.user

class Author(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.groups.filter(name='Author').exists():
            return True
        raise PermissionDenied(detail="Vous n'avez pas les permissions nécessaires pour modifier ces données.")


class Viewer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.groups.filter(name='Viewer').exists():
            return True
        raise PermissionDenied(detail="Vous n'avez pas les permissions nécessaires pour modifier ces données.")