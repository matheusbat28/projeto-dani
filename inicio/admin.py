from django.contrib import admin
from .models import Produto, Carrinho

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'preco',)
    list_display_links = ('nome',)
    search_fields = ('nome', 'descricao', 'preco', 'data_fabricacao', 'data_validacao', 'data_entrada')
    
admin.site.register(Produto, ProdutoAdmin)

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    list_display_links = ('usuario', )
    search_fields = ('usuario', )
    
admin.site.register(Carrinho, CarrinhoAdmin)