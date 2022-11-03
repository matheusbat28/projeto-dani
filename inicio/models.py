from django.db import models
from conta.models import Usuario

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    peso = models.FloatField()
    preco = models.FloatField()
    data_fabricacao = models.DateTimeField()
    data_validacao = models.DateTimeField()
    data_entrada = models.DateTimeField()
    protudo_img = models.ImageField(upload_to='produto_img/%Y/%m/%d', blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto)
    
    def __str__(self):
        return self.usuario