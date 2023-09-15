from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Evento, Favoritos
from django.http import HttpResponse, JsonResponse 
from django.conf import settings
from django.conf.urls.static import static
from .forms import EventoForm
from django.contrib import messages

# Create your views here.

def verificado(user):
    return user.groups.filter(name='Verificado').exists()

def home(request):
    if verificado(request.user):
        ver = True
    else:
        ver = False

    all_eventos = Evento.objects.all()
    response = []
    for evento in all_eventos:
        response.append({
            "id": evento.id_evento,
            "title": evento.nome_evento,
            "start": evento.data_inicio.strftime("%m/%d/%Y, %H:%M:%S"),
            "end": evento.data_final.strftime("%m/%d/%Y, %H:%M:%S"),
        })
    if request.user.is_authenticated:
        return render(request, 'home.html', {"response": response, "verificado": ver})
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

def favoritar(request, id_evento):
    user = request.user
    evento = Evento.objects.get(id_evento=id_evento)
    
    favorito_existe = Favoritos.objects.filter(id_evento=evento, id_usuario=user)

    if favorito_existe:
        favorito_existe.delete()
    else:
        Favoritos.objects.create(id_evento=evento, id_usuario=user)
    
    return redirect('abrir_evento', id_evento=id_evento)
    
def criar_evento(request):
    if request.user.is_authenticated:
        if verificado(request.user):
            if request.method == 'POST':
                form = EventoForm(request.POST, request.FILES)
                if form.is_valid():
                    evento = form.save(commit=False)
                    evento.id_usuario = request.user
                    evento.save()
                    return redirect('home')
            else:
                form = EventoForm()
                return render(request, 'evento/criar-evento.html', {'form': form})
        else:
            return redirect('home')
    else:
        return redirect('signin')


def get_eventos(request):
    get_eventos = Evento.objects.all()
    response = []
    for evento in get_eventos:
        response.append({
            'id': evento.id_evento,
            'title': evento.nome_evento,
            'id': evento.id_evento,
            'start': evento.data_inicio.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': evento.data_final.strftime("%m/%d/%Y, %H:%M:%S"),
        })

    return JsonResponse(response, safe=False) 

def abrir_evento(request,id_evento):
    evento = get_object_or_404(Evento, pk=id_evento)

    if Favoritos.objects.filter(id_evento=evento, id_usuario=request.user):
        favorito_existe = True
    else:
        favorito_existe = False

    return render(request, 'evento/evento.html', {'evento': evento ,'favorito': favorito_existe})

def editar_evento(request,id_evento):
    evento = Evento.objects.get(pk=id_evento)
    
    form = EventoForm(request.POST or None, request.FILES or None, instance=evento)
    if form.is_valid():
        form.save()
        return redirect('lista_evento')

    return render(request, 'evento/editar-evento.html', {'form': form, 'evento': evento})

def deletar_evento(request,id_evento):
    evento = Evento.objects.get(pk=id_evento)
    if not request.user.is_authenticated:
        messages.success(request, ("Você não esta logado!"))
        return redirect('lista_evento')
    elif evento.id_usuario == request.user:
        evento.delete()
        messages.success(request, ("Evento deletado com sucesso!"))
        return redirect('lista_evento')
    else:
        messages.success(request, ("Você não possui permissão para deletar este evento!"))
        return redirect('lista_evento')

def lista_evento(request):
    if request.user.is_authenticated:
        eventos = Evento.objects.filter(id_usuario=request.user)
        return render(request, 'evento/lista-evento.html', {"eventos": eventos})
    else:
        return redirect('home')

def acessar_favoritos(request):
    if request.user.is_authenticated:
        favoritos = Favoritos.objects.filter(id_usuario=request.user).select_related('id_evento')
    
    return render(request, 'evento/favoritos.html', {'favoritos': favoritos})
