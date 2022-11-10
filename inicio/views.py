from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria

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
        'categorias': Categoria.objects.all()
    }
    if request.method == "POST":
        pass
    else:
        return render(request, 'categoria/index.html', context=context)


@login_required(login_url= 'login')
def carrinho(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'carrinho/index.html')