from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from postagem import views
from postagem.api.viewsets import PostViewSet, CommentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtido'),
    path('postagem/listar_posts', views.listar_posts, name='listar_posts'),
    path('postagem/<int:post_id>/', views.detalhes_post, name='detalhes_post'),
    path('postagem/adicionar_post/', views.adicionar_post, name='adicionar_post')
]
