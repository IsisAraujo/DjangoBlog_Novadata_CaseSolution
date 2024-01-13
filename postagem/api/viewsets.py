from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied
from postagem.models import Post, Comment
from postagem.api.serializers import PostSerializer, CommentSerializer
from postagem.permissions import Permissao
import logging

# Configura um logger para este módulo específico
logger = logging.getLogger(__name__)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, Permissao]  # Define as classes de permissão

    def perform_create(self, serializer):
        # Personaliza a criação do Post para associar automaticamente o autor atual
        try:
            serializer.save(autor=self.request.user)
        except Exception as e:
            logger.error("Erro ao salvar o post: %s", str(e))
            raise  # Relança a exceção para ser tratada pelo framework


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, Permissao]  # Define as classes de permissão

    def perform_create(self, serializer):
        # Personaliza a criação do Comment para associar automaticamente o autor atual
        try:
            serializer.save(autor=self.request.user)
        except Exception as e:
            logger.error("Erro ao salvar o comentário: %s", str(e))
            raise  # Relança a exceção para ser tratada pelo framework
