from django.contrib import admin
from django.urls import path
from postagem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postagem/listar_posts', views.listar_posts, name='listar_posts'),
    path('postagem/<int:post_id>/', views.detalhes_post, name='detalhes_post'),
    path('postagem/adicionar_post/', views.adicionar_post, name='adicionar_post')
]
