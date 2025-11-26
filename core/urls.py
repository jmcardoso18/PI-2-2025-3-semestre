from django.urls import path
from .views import EventoListView 
from django.contrib.auth.views import LoginView
from core.views import api_home
from .views import lista_servicos 

urlpatterns = [
    path('eventos/', EventoListView.as_view(), name='lista_eventos'),

    path('login/', 
         LoginView.as_view(template_name='core/login.html'), 
         name='login'),

    path('api/teste/', api_home, name='api_teste'),

    path('api/servicos/', lista_servicos, name='api_servicos'),
]