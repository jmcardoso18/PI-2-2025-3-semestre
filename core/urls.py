from django.urls import path
from django.views.generic import RedirectView 

from .views import (
    lista_servicos, login_react_session, dashboard,
    cliente_lista, cliente_novo, cliente_editar, cliente_deletar,
    evento_lista, evento_novo, evento_editar, evento_deletar,
    fornecedor_lista, fornecedor_novo, fornecedor_editar, fornecedor_deletar,
    tarefa_lista, tarefa_nova, tarefa_editar, tarefa_deletar, atividade_lista, atividade_nova, atividade_editar, atividade_deletar, ocorrencia_lista, ocorrencia_nova, ocorrencia_editar, ocorrencia_deletar, servico_lista, servico_novo, servico_editar, servico_deletar, equipe_lista, equipe_nova, equipe_editar, equipe_deletar,
    colaborador_area, colaborador_home, toggle_atividade, area_cliente, toggle_tarefa, logout_react
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

    # ROTAS DE EQUIPE (ACESSOS)
    path('dashboard/equipe/', equipe_lista, name='equipe_lista'),
    path('dashboard/equipe/nova/', equipe_nova, name='equipe_nova'),
    path('dashboard/equipe/editar/<int:id>/', equipe_editar, name='equipe_editar'),
    path('dashboard/equipe/deletar/<int:id>/', equipe_deletar, name='equipe_deletar'),

    # ROTAS DE EVENTOS
    path('dashboard/eventos/', evento_lista, name='evento_lista'),
    path('dashboard/eventos/novo/', evento_novo, name='evento_novo'),
    path('dashboard/eventos/editar/<int:id>/', evento_editar, name='evento_editar'),
    path('dashboard/eventos/deletar/<int:id>/', evento_deletar, name='evento_deletar'),

    # ROTAS DE FORNECEDORES
    path('dashboard/fornecedores/', fornecedor_lista, name='fornecedor_lista'),
    path('dashboard/fornecedores/novo/', fornecedor_novo, name='fornecedor_novo'),
    path('dashboard/fornecedores/editar/<int:id>/', fornecedor_editar, name='fornecedor_editar'),
    path('dashboard/fornecedores/deletar/<int:id>/', fornecedor_deletar, name='fornecedor_deletar'),

    # ROTAS DE TAREFAS
    path('dashboard/tarefas/', tarefa_lista, name='tarefa_lista'),
    path('dashboard/tarefas/nova/', tarefa_nova, name='tarefa_nova'),
    path('dashboard/tarefas/editar/<int:id>/', tarefa_editar, name='tarefa_editar'),
    path('dashboard/tarefas/deletar/<int:id>/', tarefa_deletar, name='tarefa_deletar'),

    # ROTAS DE ATIVIDADES
    path('dashboard/atividades/', atividade_lista, name='atividade_lista'),
    path('dashboard/atividades/nova/', atividade_nova, name='atividade_nova'),
    path('dashboard/atividades/editar/<int:id>/', atividade_editar, name='atividade_editar'),
    path('dashboard/atividades/deletar/<int:id>/', atividade_deletar, name='atividade_deletar'),

    # ROTAS DE OCORRÊNCIAS
    path('dashboard/ocorrencias/', ocorrencia_lista, name='ocorrencia_lista'),
    path('dashboard/ocorrencias/nova/', ocorrencia_nova, name='ocorrencia_nova'),
    path('dashboard/ocorrencias/editar/<int:id>/', ocorrencia_editar, name='ocorrencia_editar'),
    path('dashboard/ocorrencias/deletar/<int:id>/', ocorrencia_deletar, name='ocorrencia_deletar'),

    # ROTAS DE SERVIÇOS
    path('dashboard/servicos/', servico_lista, name='servico_lista'),
    path('dashboard/servicos/novo/', servico_novo, name='servico_novo'),
    path('dashboard/servicos/editar/<int:id>/', servico_editar, name='servico_editar'),
    path('dashboard/servicos/deletar/<int:id>/', servico_deletar, name='servico_deletar'),

    # Área do Colaborador
    path('colaborador/home/', colaborador_home, name='colaborador_home'),
    path('colaborador/evento/<int:evento_id>/', colaborador_area, name='colaborador_area'),
    
    # API Checkbox
    path('api/toggle-atividade/<int:id>/', toggle_atividade, name='toggle_atividade'),

    # Rota da Área do Cliente
    path('area-cliente/', area_cliente, name='area_cliente'),
    
    # API para checkbox de tarefa
    path('api/toggle-tarefa/<int:id>/', toggle_tarefa, name='toggle_tarefa'),
    path('api/logout/', logout_react, name='logout_react'),
]