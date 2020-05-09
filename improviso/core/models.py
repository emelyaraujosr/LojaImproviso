from django.db import models

# Create your models here.

class Produtos (models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('price', decimal_places=2, max_digits=6)
    estoque = models.IntegerField('estoque')