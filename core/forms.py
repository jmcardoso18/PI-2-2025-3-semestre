from django import forms
from .models import Usuario
from .models import Usuario, Evento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'celular', 'tipo', 'pix'] # Adicionei 'senha' aqui
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'exemplo@email.com'
            }),
            # CAMPO DE SENHA (NOVO)
            'senha': forms.PasswordInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Defina uma senha de acesso',
                'render_value': True # Mantém a senha se der erro no form (opcional)
            }),
            'celular': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': '(XX) XXXXX-XXXX'
            }),
            'tipo': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Ex: Noiva, Debutante'
            }),
            'pix': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Chave PIX (opcional)'
            }),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['usuario', 'nome', 'data', 'local', 'tipo', 'estimativa_convidados']
        
        widgets = {
            'usuario': forms.Select(attrs={
                'class': 'w-full rounded-lg border-neutral-300 bg-white px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition'
            }),
            'nome': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Ex: Casamento Maria e João'
            }),
            'data': forms.DateInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'type': 'date' 
            }),
            'local': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Nome do Salão/Igreja'
            }),
            'tipo': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Ex: Casamento, 15 anos'
            }),
            'estimativa_convidados': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Qtd. Estimada'
            }),
        }
    
    # Filtra apenas usuários do tipo 'cliente'
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)