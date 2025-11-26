from django.shortcuts import render
from django.views.generic import ListView
from .models import Evento
from django.http import JsonResponse
from .models import Servico

# Create your views here.

class EventoListView(ListView):
    model = Evento
    
    # O nome do arquivo HTML que vamos criar na Etapa 3
    template_name = 'core/lista_eventos.html'
    
    # O nome da variável que usaremos no HTML (ex: 'for evento in eventos')
    context_object_name = 'eventos'

def api_home(request):
    dados = {
        "mensagem": "Olá, React! Eu sou o Django.",
        "usuario": "Felipe",
        "status": "Conectado"
    }
    return JsonResponse(dados)

# View para a página inicial (se você usar templates do Django)
def home(request):
    return render(request, 'index.html') # ou o nome do seu template

# --- API PARA O REACT ---
def lista_servicos(request):
    # Pega todos os serviços do banco
    servicos = Servico.objects.all().values('id', 'titulo', 'descricao', 'preco')
    
    # Transforma em lista Python
    dados = list(servicos)
    
    # Retorna como JSON
    return JsonResponse(dados, safe=False)