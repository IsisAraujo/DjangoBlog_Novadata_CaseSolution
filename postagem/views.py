from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from postagem.forms import PostagemForm


def listar_posts(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'listar_posts.html', {'posts': posts})


def detalhes_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detalhes_post.html', {'post': post})


def adicionar_post(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')  # Redireciona para a lista de posts após o salvamento
    else:
        form = PostagemForm()
    return render(request, 'adicionar_post.html', {'form': form})
