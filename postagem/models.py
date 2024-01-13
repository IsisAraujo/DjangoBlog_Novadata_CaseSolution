from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='título')
    conteudo = models.TextField(verbose_name='conteúdo')
    data_publicacao = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Comment(models.Model):
    # varios autores
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField(verbose_name='conteúdo')
    data_criacao = models.DateTimeField(default=timezone.now)
    # varias publicacoes
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.post.titulo}'
