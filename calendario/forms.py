from django import forms
from .models import Evento
from django.forms import Textarea, TextInput, DateTimeInput, Select, NumberInput

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome_evento', 'descricao', 'data_inicio', 'data_final', 'local_online', 'faixa_etaria', 'endereco', 'website', 'politica', 'banner']
        labels = {
            'nome_evento': 'Nome do Evento',
            'descricao': 'Descrição',
            'data_inicio': 'Data de Inicio',
            'data_final': 'Data de Final',
            'local_online': 'Local ou Online?',
            'faixa_etaria': 'Idade Mínima',
            'endereco': 'Endereço',
            'website': 'Website',
            'politica': 'Política do evento',
            'banner': 'Banner do Evento',
        }
        widgets = {
            'nome_evento': TextInput(attrs=({"class": "form-control"})),
            'descricao': Textarea(attrs=({"class": "form-control"})),
            'endereco': TextInput(attrs=({"class": "form-control"})),
            'website': TextInput(attrs=({"class": "form-control"})),
            'politica': TextInput(attrs=({"class": "form-control"})),
            'data_inicio': DateTimeInput(attrs=({"class": "form-control","type":"datetime-local"})),
            'data_final': DateTimeInput(attrs=({"class": "form-control","type":"datetime-local"})),
            'local_online': Select(attrs=({"class": "form-control"})),
            'faixa_etaria': NumberInput(attrs=({"class": "form-control"})),
        }
