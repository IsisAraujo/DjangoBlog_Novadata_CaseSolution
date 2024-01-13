from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import AccessToken


# Classe de teste para autenticação na API
class AutenticacaoTeste(APITestCase):

    def setUp(self):
        # Criação de um usuário para teste
        self.username = "usuario_teste"
        self.password = "senha_segura"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_acesso_sem_autenticacao(self):
        # Testa se o acesso sem autenticação é negado
        url = reverse('post-list')  # Endereço da API para listar posts
        resposta = self.client.post(url, {})
        self.assertEqual(resposta.status_code, status.HTTP_401_UNAUTHORIZED)  # Verifica se o acesso é negado

    def test_acesso_com_autenticacao(self):
        # Testa se o acesso com autenticação é permitido
        token = AccessToken.for_user(self.user)  # Gera um token JWT para o usuário
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {str(token)}')  # Configura o token de autenticação no cabeçalho
        url = reverse('post-list')  # Endereço da API para listar posts
        resposta = self.client.post(url, {})
        self.assertNotEqual(resposta.status_code, status.HTTP_401_UNAUTHORIZED)  # Verifica se o acesso é permitido
