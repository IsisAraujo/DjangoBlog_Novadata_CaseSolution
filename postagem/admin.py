from django.contrib import admin
from postagem.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao')
    list_filter = ('data_publicacao', 'autor')
    search_fields = ('titulo', 'conteudo')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'autor', 'data_criacao', 'conteudo')
    list_filter = ('data_criacao', 'autor')
    search_fields = ('conteudo',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
