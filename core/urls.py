from django.urls import path
from .views import EventoListView 
from django.contrib.auth.views import LoginView

urlpatterns = [
    # Quando o usuário acessar 'eventos/', vamos mostrar a EventoListView
    path('eventos/', EventoListView.as_view(), name='lista_eventos'),

    path('login/', 
         LoginView.as_view(template_name='core/login.html'), 
         name='login'),
]