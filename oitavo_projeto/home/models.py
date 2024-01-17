from django.db import models

class Livro(models.Model):
    nome_livro = models.CharField(max_length=60)
    ano_publicacao = models.IntegerField()
    quantidade_pag = models.IntegerField()
    nome_autor = models.CharField(max_length=100)
    nome_editora = models.CharField(max_length=100)
    preco = models.FloatField(default=0.00)

    def __str__(self):
        return self.nome_livro
