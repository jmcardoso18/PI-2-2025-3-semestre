from django import forms
from .models import Usuario
from .models import Usuario, Evento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'celular', 'tipo', 'pix']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'exemplo@email.com'}),
            'celular': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '(XX) XXXXX-XXXX'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),  
            'pix': forms.TextInput(attrs={'class': 'form-input'}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['usuario', 'nome', 'data', 'local', 'tipo', 'convidados']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Casamento Maria e João'}),
            'data': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}), # Calendário
            'local': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nome do Salão/Igreja'}),
            'tipo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ex: Casamento, 15 anos'}),
            'convidados': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Qtd. Estimada'}),
        }
    
    # Filtra apenas usuários do tipo 'cliente'
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)