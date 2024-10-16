from rest_framework import permissions

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
