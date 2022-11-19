from django.db import models
from conta.models import Usuario


class Categoria(models.Model):
    tpCategoria = models.CharField(max_length=255)
    categoria_img = models.ImageField(upload_to='categoria_img/%Y/%m/%d')
    
    def __str__(self):
        return self.tpCategoria


class Marca(models.Model):
    marca = models.CharField(max_length=255)
    
    def __str__(self):
        return self.marca

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    peso = models.FloatField(blank=True, null=True)
    preco = models.FloatField()
    data_fabricacao = models.DateTimeField()
    data_validacao = models.DateTimeField()
    data_entrada = models.DateTimeField(auto_now_add = True)
    protudo_img = models.ImageField(upload_to='produto_img/%Y/%m/%d', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.DO_NOTHING)
    marca = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    quantidade_produto = models.IntegerField()
    valorTotal = models.FloatField(blank=True, null=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.usuario.get_username()

