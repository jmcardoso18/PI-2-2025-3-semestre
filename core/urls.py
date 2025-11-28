from django.urls import path
from .views import lista_servicos, login_react_session, dashboard

urlpatterns = [
    # --- APIs para o Front-end (React) ---
    path('api/servicos/', lista_servicos, name='api_servicos'),
    path('api/login-session/', login_react_session, name='login_session'),

    # --- Área do Cliente (Django Templates) ---
    path('dashboard/', dashboard, name='dashboard'),
]