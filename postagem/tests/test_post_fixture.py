from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth.models import User
from postagem.models import Post

# Classe de teste para o modelo Post
class PostTestCase(TestCase):

    def setUp(self):
        # Configuração inicial do teste
        # Cria um usuário de teste
        User.objects.create(id=2, username='teste')
        # Carrega dados de teste do arquivo fixture JSON para o banco de dados de teste
        call_command('loaddata', 'postagem/posts_fixture.json')

    def test_post_existente(self):
        # Teste para verificar se um post específico existe e tem o título correto
        post = Post.objects.get(pk=1)  # Obtém o post com id 1
        self.assertEqual(post.titulo, "Post 1")  # Verifica se o título do post é "Post 1"
