from django.urls import path
from django.views.generic import RedirectView 

from .views import (
    lista_servicos, login_react_session, dashboard,
    cliente_lista, cliente_novo, cliente_editar, cliente_deletar,
    evento_lista, evento_novo, evento_editar, evento_deletar,
    colaborador_area, toggle_atividade, area_cliente, toggle_tarefa, logout_react
)

urlpatterns = [
    # --- ROTA RAIZ ---
    path('', RedirectView.as_view(url='/dashboard/')),

    # --- APIs para o Front-end (React) ---
    path('api/servicos/', lista_servicos, name='api_servicos'),
    path('api/login-session/', login_react_session, name='login_session'),

    # --- Área do Cliente (Django Templates) ---
    path('dashboard/', dashboard, name='dashboard'),

    # ROTAS DE CLIENTES
    path('dashboard/clientes/', cliente_lista, name='cliente_lista'),
    path('dashboard/clientes/novo/', cliente_novo, name='cliente_novo'),
    path('dashboard/clientes/editar/<int:id>/', cliente_editar, name='cliente_editar'),
    path('dashboard/clientes/deletar/<int:id>/', cliente_deletar, name='cliente_deletar'),

    # ROTAS DE EVENTOS
    path('dashboard/eventos/', evento_lista, name='evento_lista'),
    path('dashboard/eventos/novo/', evento_novo, name='evento_novo'),
    path('dashboard/eventos/editar/<int:id>/', evento_editar, name='evento_editar'),
    path('dashboard/eventos/deletar/<int:id>/', evento_deletar, name='evento_deletar'),

    # Área do Colaborador
    path('colaborador/evento/<int:evento_id>/', colaborador_area, name='colaborador_area'),
    
    # API Checkbox
    path('api/toggle-atividade/<int:id>/', toggle_atividade, name='toggle_atividade'),

    # Rota da Área do Cliente
    path('area-cliente/', area_cliente, name='area_cliente'),
    
    # API para checkbox de tarefa
    path('api/toggle-tarefa/<int:id>/', toggle_tarefa, name='toggle_tarefa'),
    path('api/logout/', logout_react, name='logout_react'),
]