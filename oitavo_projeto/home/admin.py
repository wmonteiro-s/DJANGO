from django.contrib import admin
from .models import Livro

class ListLivro(admin.ModelAdmin):
    list_display = ('nome_livro', 'ano_publicacao', 'quantidade_pag', 'nome_autor', 'nome_editora', 'preco')

admin.site.register(Livro, ListLivro)
