from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from postagem.tests.factories import PostFactory, UsuarioFactory, CommentFactory


# Classe de teste para a API de Post
class PostAPITestCase(APITestCase):
    def setUp(self):
        # Configuração inicial: cria um post e um usuário para os testes
        self.post = PostFactory()
        self.usuario = UsuarioFactory()

    def test_listar_posts(self):
        # Testa a listagem de posts
        url = reverse('post-list')
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resposta.data), 1)  # Verifica se há um post na resposta

    def test_obter_post(self):
        # Testa a obtenção de detalhes de um post específico
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta.data['titulo'], self.post.titulo)  # Verifica se o título corresponde


# Classe de teste para a API de Comment
class CommentAPITestCase(APITestCase):
    def setUp(self):
        # Configuração inicial: cria um comentário e um usuário para os testes
        self.comment = CommentFactory()
        self.usuario = UsuarioFactory()

    def test_listar_comentarios(self):
        # Testa a listagem de comentários
        url = reverse('comment-list')
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resposta.data), 1)  # Verifica se há um comentário na resposta

    def test_obter_comentario(self):
        # Testa a obtenção de detalhes de um comentário específico
        url = reverse('comment-detail', kwargs={'pk': self.comment.pk})
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        self.assertEqual(resposta.data['conteudo'], self.comment.conteudo)  # Verifica se o conteúdo corresponde
