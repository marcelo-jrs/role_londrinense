"""
URL configuration for role_londrinense project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from calendario import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro/', views.signup, name='signup'),
    path('entrar/', views.signin, name='signin'),
    path('sair/', views.signout, name='signout'),
    path('criar-evento/', views.criar_evento, name='criar_evento'),
    path('all_events/', views.get_eventos, name='get_eventos'),
    path('evento/<int:id_evento>/', views.abrir_evento, name='abrir_evento'),
    path('editar-evento/<int:id_evento>/', views.editar_evento, name='editar_evento'),
    path('deletar-evento/<int:id_evento>/', views.deletar_evento, name='deletar_evento'),
    path('meus-eventos/', views.lista_evento, name='lista_evento'),
    path('favorito/<int:id_evento>/', views.favoritar, name='favoritar'),
    path('favoritos/', views.acessar_favoritos, name='acessar_favoritos'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
