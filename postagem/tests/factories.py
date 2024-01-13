import factory
from django.contrib.auth.models import User
from postagem.models import Post, Comment
from django.utils import timezone


# Factory para criar instâncias do modelo User
class UsuarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'usuario{n}')  # Gera nomes de usuário únicos
    password = factory.PostGenerationMethodCall('set_password', '12345')  # Define a senha


# Factory para criar instâncias do modelo Post
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    titulo = factory.Faker('sentence')  # Gera um título fictício
    conteudo = factory.Faker('text')  # Gera conteúdo fictício
    autor = factory.SubFactory(UsuarioFactory)  # Associa um autor usando UsuarioFactory
    data_publicacao = factory.LazyFunction(timezone.now)  # Define a data de publicação para agora


# Factory para criar instâncias do modelo Comment
class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    autor = factory.SubFactory(UsuarioFactory)  # Associa um autor usando UsuarioFactory
    conteudo = factory.Faker('text')  # Gera conteúdo fictício para o comentário
    data_criacao = factory.LazyFunction(timezone.now)  # Define a data de criação para agora
    post = factory.SubFactory(PostFactory)  # Associa um post usando PostFactory
