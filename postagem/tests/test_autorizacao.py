from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import AccessToken

from postagem.tests.factories import PostFactory


class AutorizacaoTeste(APITestCase):

    def setUp(self):
        self.autor = User.objects.create_user(username='autor', password='senha123')
        self.outro_usuario = User.objects.create_user(username='outro_usuario', password='senha123')
        self.post = PostFactory(autor=self.autor)

    def test_autor_pode_editar_post(self):
        token = AccessToken.for_user(self.autor)  # Gera um token para o autor
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token))
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        dados = {'titulo': 'Título Atualizado', 'conteudo': 'Conteúdo Atualizado'}
        resposta = self.client.put(url, dados, format='json')
        print(resposta.data)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)

    def test_outro_usuario_nao_pode_editar_post(self):
        self.client.login(username='outro_usuario', password='senha123')
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        dados = {'titulo': 'Título Atualizado', 'conteudo': 'Conteúdo Atualizado'}
        resposta = self.client.put(url, dados, format='json')
        self.assertNotEqual(resposta.status_code, status.HTTP_200_OK)

    def test_usuario_nao_autenticado_nao_pode_editar_post(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        dados = {'titulo': 'Título Atualizado', 'conteudo': 'Conteúdo Atualizado'}
        resposta = self.client.put(url, dados, format='json')
        self.assertEqual(resposta.status_code, status.HTTP_401_UNAUTHORIZED)
