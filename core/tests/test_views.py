from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Usuario, Evento
from datetime import date

class ViewSecurityTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Admin
        self.admin_user = User.objects.create_user(username='admin', email='admin@teste.com', password='123', is_staff=True)
        
        # Cliente
        self.cliente_user = User.objects.create_user(username='cliente@teste.com', email='cliente@teste.com', password='123', is_staff=False)
        self.perfil_cliente = Usuario.objects.create(nome="Cliente", email="cliente@teste.com", tipo="Noiva")
        
        # Evento
        Evento.objects.create(usuario=self.perfil_cliente, nome="Festa", data=date(2026,1,1), local="X", tipo="Y", estimativa_convidados="100")

    def test_dashboard_acesso_admin(self):
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_bloqueio_cliente(self):
        self.client.login(username='cliente@teste.com', password='123')
        response = self.client.get(reverse('dashboard'))
        # Deve redirecionar (302)
        self.assertEqual(response.status_code, 302)

    def test_area_cliente_acesso(self):
        self.client.login(username='cliente@teste.com', password='123')
        response = self.client.get(reverse('area_cliente'))
        self.assertEqual(response.status_code, 200)
        # Verifica se o nome do evento aparece no HTML
        self.assertContains(response, "Festa")

    def test_anonimo_nao_acessa_nada(self):
        response = self.client.get(reverse('dashboard'))
        # Deve redirecionar (302) para o login externo
        self.assertEqual(response.status_code, 302)
        self.assertTrue("login" in response.url)