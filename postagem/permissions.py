from rest_framework import permissions


# Classe personalizada de permissão
class Permissao(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Permite métodos de leitura seguros (GET, HEAD, OPTIONS) para qualquer solicitação
        if request.method in permissions.SAFE_METHODS:
            return True

        # Garante que o objeto só possa ser editado pelo autor
        # Isso restringe as operações de escrita (POST, PUT, DELETE) ao autor do objeto
        return obj.autor == request.user
