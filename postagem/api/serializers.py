from rest_framework import serializers
from postagem.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'titulo', 'conteudo', 'autor', 'data_publicacao']
        read_only_fields = ['autor']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'autor', 'conteudo', 'data_criacao', 'post']
