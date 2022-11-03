from django.shortcuts import render, redirect
from django.contrib import messages
from conta.models import Usuario
from django.db import utils
from django.contrib.auth.hashers import make_password
from django.contrib import auth, messages

def login(request):
    auth.logout(request)
    if request.method == 'POST':
        pass
    else:
        return render(request, 'login/index.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome').strip()
        sobrenome = request.POST.get('sobrenome').strip()
        usuario = request.POST.get('usuario').strip()
        telefone = request.POST.get('telefone').strip()
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha').strip()
        
        if len(nome) <= 3:
            messages.error(request, 'Nome muito curto')
            return redirect('cadastro')
        elif len(sobrenome) <= 3:
            messages.error(request, 'sobrenome muito curto')
            return redirect('cadastro')
        elif len(usuario) <= 3:
            messages.error(request, 'usuário muito curto')
            return redirect('cadastro')
        elif len(telefone) <= 14:
            messages.error(request, 'telefone muito curto')
            return redirect('cadastro')
        elif len(senha) <= 8:
            messages.error(request, 'senha muito curto')
            return redirect('cadastro')
        else:
            try:
                Usuario.objects.create(first_name = nome,
                                    last_name = sobrenome,
                                    username = usuario,
                                    email = email,
                                    password = make_password(senha),
                                    telefone = telefone)               
            except utils.IntegrityError:
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')
            
            return redirect('login')
    else:
        return render(request, 'cadastro/index.html')



def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario').strip()
        senha = request.POST.get('senha').strip()
        check = auth.authenticate(request, username=usuario, password=senha)

        if check is not None:
            auth.login(request, check)
            return redirect('home') #Ajustar após adicionar o HTML da home

        else:
            messages.error(request, "Usuario ou Senha Incorretos!!")
            return redirect('login')  
 
    else:      
        return render(request, 'login/index.html')