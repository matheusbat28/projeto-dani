from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria, Carrinho
from conta.models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q

@login_required(login_url= 'login')
def home(request):
    context = {
        'produtos': Produto.objects.all(),
        'categorias': Categoria.objects.all(),
    }
    if request.method == "POST":
        pass
    else:

        return render(request, 'home/index.html', context=context)

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
    carrinhos = Carrinho.objects.filter(status = False, usuario = request.user.id)
    valor = 0
    for carrinho in carrinhos:
        valor += carrinho.produto.preco * carrinho.quantidade_produto

    if request.method == "POST":
        
        for carrinho in carrinhos:  
            valores = '{:.2f}'.format(carrinho.produto.preco * carrinho.quantidade_produto)
            produto = Produto.objects.get(id = carrinho.produto.id)
            produto.quantidade -= carrinho.quantidade_produto

            carrinho.status = True
            carrinho.valorTotal = valores
            produto.save()
            carrinho.save()
        
        return redirect('carrinho')
    else:
        return render(request, 'carrinho/index.html', {'carrinhos':carrinhos, 'valor':valor})

@login_required(login_url= 'login')
def deletarCart(request, id):
    if Carrinho.objects.get(id=id):
        Carrinho.objects.get(id=id).delete()
        return redirect('carrinho')
    else:
        return redirect('carrinho')
    
@login_required(login_url= 'login')
def produtos(request):
    context = {
        'produtos': Produto.objects.all(),
    }
    if request.method == "POST":
        produt = Produto.objects.get(id = request.POST.get('btCart'))
        qtdProduto = request.POST.get('qtdProduto')
        Carrinho.objects.create(produto_id = produt.id, usuario_id=request.user.id, quantidade_produto=qtdProduto)
        return redirect('produtos')
    else:
        return render(request, 'produtos/index.html', context=context)
    
@login_required(login_url= 'login')
def perfil(request):
    usuario = Usuario.objects.get(id=request.user.id)
    if request.method == "POST":
        msg = ''
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')
        img = request.FILES.get('image')
        if first_name != usuario.first_name:
            usuario.first_name = first_name
            msg +="Usuario,"
        if last_name != usuario.last_name:
            usuario.last_name = last_name  
            msg +="Ultimo Nome, " 
        if telefone != usuario.telefone:
            usuario.telefone = telefone 
            msg +="Telefone, "    
        if email != usuario.email:
            usuario.email = email  
            msg +="Email,"   
        if img != '':
            usuario.perfil_img = img    
            msg +="Foto,"   
        if senha1 == senha2 and senha1 != '' and senha2 != '':
            if len(senha1) <= 8 and len(senha1) >=4:
                usuario.password = make_password(senha1)
                usuario.save()
                msg +="Senha," 
                
            else:    
                usuario.save()
        usuario.save()  
        messages.success(request , msg + ' - Foram Salvos')              
        return redirect('perfil')
    else:

        return render(request, 'perfil/index.html', {'usuario':usuario})        

@login_required(login_url= 'login')
def buscar(request):
    busca = request.GET.get('buscar')
    context = {
        'produtos': Produto.objects.filter(Q(nome__icontains=busca) | Q(descricao__icontains=busca)),
    }
    return render(request, 'produtos/index.html', context=context)