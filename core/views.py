from django.shortcuts import render
from django.views.generic import ListView
from .models import Evento

# Create your views here.

class EventoListView(ListView):
    model = Evento
    
    # O nome do arquivo HTML que vamos criar na Etapa 3
    template_name = 'core/lista_eventos.html'
    
    # O nome da variável que usaremos no HTML (ex: 'for evento in eventos')
    context_object_name = 'eventos'