from django import forms
from .models import Evento
from django.forms import Textarea, TextInput, DateTimeInput, Select, NumberInput, FileInput

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        endereco = forms.CharField(max_length=255, required=False)
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
            'banner': FileInput(attrs=({"class": "form-control"})),
        }

    def clean_nome_evento(self):
        nome_evento = self.cleaned_data['nome_evento']
        if len(nome_evento.strip()) == 0 or nome_evento.isdigit() or len(nome_evento) > 100:
            raise forms.ValidationError('O nome do evento deve conter entre 1 e 100 caracteres e não pode ser somente números ou espaços.')
        return nome_evento

    def clean_descricao(self):
        descricao = self.cleaned_data['descricao']
        if len(descricao) < 20:
            raise forms.ValidationError('A descrição deve conter pelo menos 20 caracteres.')
        return descricao

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_final = cleaned_data.get('data_final')

        if data_inicio and data_final and data_inicio >= data_final:
            raise forms.ValidationError('A data de início deve acontecer antes da data final.')

        local_online = cleaned_data.get('local_online')
        endereco = cleaned_data.get('endereco')

        if not local_online:
            raise forms.ValidationError('O campo "Local ou Online?" é obrigatório.')

        if local_online == 'Local' and not endereco:
            raise forms.ValidationError('O campo "Endereço" é obrigatório quando o evento é local.')
