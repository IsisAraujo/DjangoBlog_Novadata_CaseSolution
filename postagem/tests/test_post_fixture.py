from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth.models import User


class PostTestCase(TestCase):

    def setUp(self):
        User.objects.create(id=2, username='teste')
        call_command('loaddata', 'postagem/posts_fixture.json')
    def test_post_existente(self):
        from postagem.models import Post
        post = Post.objects.get(pk=1)
        self.assertEqual(post.titulo, "Post 1")
