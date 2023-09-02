from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Evento


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['senha']
        )

        if user.is_authenticated:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuário ou senha incorretos'
            })

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['confirmarSenha'] == request.POST['senha']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                               first_name=request.POST['nome'],
                                               last_name=request.POST['sobrenome'],
                                               email=request.POST['email'],
                                               password=request.POST['senha'])
                user.save()
                login(request, user)
                return redirect('signin')
            except:
                return render(request, 'signup.html', {
                            'form' : UserCreationForm,
                            'error' : 'Usuário Já Existe'
                            })
            
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'As senhas são diferentes'
        })

def signout(request):
    logout(request)
    return redirect('signin')

def createEvento(request):
    if request.method == 'GET':
        return render(request, 'evento-create.html')
    elif request.method == 'POST':
        evento = Evento()
        evento.nome_evento = request.POST['nome_evento']
        evento.descricao = request.POST['descricao']
        evento.data_inicio = request.POST['data_inicio']
        evento.data_final = request.POST['data_final']
        evento.local_online = request.POST['local_online']
        evento.faixa_etaria = request.POST['faixa_etaria']
        evento.id_usuario = request.user

        evento.save()
        return redirect('home')