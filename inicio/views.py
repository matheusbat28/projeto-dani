from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria, Carrinho

@login_required(login_url= 'login')
def home(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'home/index.html')

@login_required(login_url= 'login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url= 'login')
def categoria(request):

    context = {
        'produtos': Produto.objects.all(),
        'categorias': Categoria.objects.raw('select ic.id, ic.tpCategoria from inicio_produto ip left join inicio_categoria ic on ic.id = ip.categoria_id group by ic.id, ic.tpCategoria')
    }
    if request.method == "POST":
        produt = Produto.objects.get(id = request.POST.get('btCart'))
        qtdProduto = request.POST.get('qtdProduto')
        Carrinho.objects.create(produto_id = produt.id, usuario_id=request.user.id, quantidade_produto=qtdProduto)
        return redirect('categoria')
    else:
        return render(request, 'categoria/index.html', context=context)


@login_required(login_url= 'login')
def carrinho(request):
    carrinhos = Carrinho.objects.filter(usuario_id=request.user.id)
    valor = 0
    for carrinho in carrinhos:
        valor += carrinho.produto.preco * carrinho.quantidade_produto

    if request.method == "POST":
        pass
    else:
        return render(request, 'carrinho/index.html', {'carrinhos':carrinhos, 'valor':valor})