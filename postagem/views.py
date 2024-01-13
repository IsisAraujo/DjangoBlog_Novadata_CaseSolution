from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from postagem.forms import PostagemForm
import logging
from django.views.decorators.cache import cache_page

logger = logging.getLogger(__name__)


@cache_page(60 * 20)  # Cache por 20 minutos
def listar_posts(request):
    try:
        posts = Post.objects.all().order_by('-data_publicacao')
    except Exception as e:
        logger.error("Erro ao listar posts: %s", str(e))
        messages.error(request, "Ocorreu um erro ao listar os posts.")
        posts = []
    return render(request, 'listar_posts.html', {'posts': posts})


def detalhes_post(request, post_id):
    try:
        post = get_object_or_404(Post.objects.prefetch_related('comentarios'), pk=post_id)

    except Exception as e:
        logger.error("Erro ao acessar detalhes do post: %s", str(e))
        messages.error(request, "Post não encontrado.")
        return redirect('listar_posts')
    return render(request, 'detalhes_post.html', {'post': post})


def adicionar_post(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Post adicionado com sucesso.")
                return redirect('listar_posts')
            except Exception as e:
                logger.error("Erro ao adicionar post: %s", str(e))
                messages.error(request, "Ocorreu um erro ao adicionar o post.")
    else:
        form = PostagemForm()
    return render(request, 'adicionar_post.html', {'form': form})
