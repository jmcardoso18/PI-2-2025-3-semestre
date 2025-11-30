from django import forms
from .models import Usuario
from .models import Usuario, Evento, Fornecedor, Tarefa, Atividade, Ocorrencia, Servico

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

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'celular', 'tipo', 'pix']
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Nome do Profissional'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'email@equipe.com'
            }),
            'senha': forms.PasswordInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Senha de acesso',
                'render_value': True
            }),
            'celular': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': '(XX) XXXXX-XXXX'
            }),
            # Sugestões de cargos para a equipe
            'tipo': forms.Select(choices=[
                ('Cerimonialista', 'Cerimonialista (Admin)'),
                ('Colaborador', 'Colaborador / Staff'),
                ('Fotógrafo', 'Fotógrafo'),
                ('Buffet', 'Buffet'),
                ('Segurança', 'Segurança'),
                ('Outro', 'Outro')
            ], attrs={
                'class': 'w-full rounded-lg border-neutral-300 bg-white px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition'
            }),
            'pix': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Chave PIX para pagamento'
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


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['evento', 'empresa', 'servico', 'status']
        
        widgets = {
            'evento': forms.Select(attrs={
                'class': 'w-full rounded-lg border-neutral-300 bg-white px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition'
            }),
            'empresa': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Nome da Empresa ou Profissional'
            }),
            'servico': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Ex: Buffet, Fotografia, Decoração'
            }),
            # Criamos um Select manual para o status ficar bonito
            'status': forms.Select(choices=[
                ('Pendente', 'Pendente'),
                ('Em negociação', 'Em negociação'),
                ('Confirmado', 'Confirmado'),
                ('Cancelado', 'Cancelado')
            ], attrs={
                'class': 'w-full rounded-lg border-neutral-300 bg-white px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition'
            }),
        }

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['evento', 'titulo', 'descricao', 'data_limite', 'feito']
        
        widgets = {
            'evento': forms.Select(attrs={
                'class': 'w-full rounded-lg border-neutral-300 bg-white px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition'
            }),
            'titulo': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Ex: Escolher o vestido'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'rows': 3,
                'placeholder': 'Detalhes da tarefa...'
            }),
            'data_limite': forms.DateInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'type': 'date'
            }),
            'feito': forms.CheckboxInput(attrs={
                'class': 'rounded border-gray-300 text-black focus:ring-black h-5 w-5'
            }),}
        
class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['evento', 'nome', 'horario', 'feito']
        
        widgets = {
            'evento': forms.Select(attrs={
                'class': 'w-full rounded-lg border-neutral-300 bg-white px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition'
            }),
            'nome': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Ex: Cerimônia, Valsa, Jantar'
            }),
            'horario': forms.TimeInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'type': 'time' # Seletor de Hora
            }),
            'feito': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 rounded border-neutral-300 text-black focus:ring-black transition cursor-pointer'
            }),
        }

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['evento', 'tipo', 'descricao']
        
        widgets = {
            'evento': forms.Select(attrs={
                'class': 'w-full rounded-lg border-neutral-300 bg-white px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition'
            }),
            # Sugestões de tipos de ocorrência
            'tipo': forms.Select(choices=[
                ('Atraso', 'Atraso'),
                ('Dano Material', 'Dano Material'),
                ('Reclamação', 'Reclamação'),
                ('Solicitação Extra', 'Solicitação Extra'),
                ('Outro', 'Outro')
            ], attrs={
                'class': 'w-full rounded-lg border-neutral-300 bg-white px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Descreva o que aconteceu...',
                'rows': 4
            }),
        }

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['titulo', 'preco', 'descricao']
        
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Nome do Pacote (Ex: Assessoria Completa)'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Valor (Ex: 1500.00)',
                'step': '0.01'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border-neutral-300 px-4 py-2.5 text-sm focus:border-black focus:ring-black shadow-sm transition',
                'placeholder': 'Descreva o que está incluso no pacote...',
                'rows': 5
            }),
        }