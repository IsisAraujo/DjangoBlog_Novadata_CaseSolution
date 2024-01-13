from rest_framework import serializers
from postagem.models import Post, Comment


# Serializador para o modelo Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'titulo', 'conteudo', 'autor', 'data_publicacao']
        read_only_fields = ['autor']  # Define 'autor' como um campo somente leitura


# Serializador para o modelo Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'autor', 'conteudo', 'data_criacao', 'post']
