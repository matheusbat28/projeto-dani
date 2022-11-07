from django.contrib import admin
from .models import Produto, Carrinho, Categoria, Marca

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'preco', 'categoria', 'marca')
    list_display_links = ('nome',)
    search_fields = ('nome', 'descricao', 'preco','categoria', 'marca')
    
admin.site.register(Produto, ProdutoAdmin)

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    list_display_links = ('usuario', )
    search_fields = ('usuario', )
    
admin.site.register(Carrinho, CarrinhoAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('tpCategoria',)
    list_display_links = ('tpCategoria', )
    search_fields = ('tpCategoria', )

admin.site.register(Categoria, CategoriaAdmin)    

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('marca',)
    list_display_links = ('marca', )
    search_fields = ('marca', )

admin.site.register(Marca, MarcaAdmin)    