from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Usuario, Evento, Tarefa
from datetime import date

class ApiLogicTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Cria usuários
        self.admin = User.objects.create_user(username='admin', email='admin@teste.com', password='123', is_staff=True)
        
        # Colaborador precisa do perfil Usuario para o redirecionamento funcionar
        self.user_colab = User.objects.create_user(username='staff@teste.com', email='staff@teste.com', password='123')
        Usuario.objects.create(nome="Staff", email="staff@teste.com", tipo="Colaborador")

        # Cliente
        self.user_cliente = User.objects.create_user(username='noiva@teste.com', email='noiva@teste.com', password='123')
        perfil = Usuario.objects.create(nome="Noiva", email="noiva@teste.com", tipo="Noiva")
        
        # Dados
        self.evento = Evento.objects.create(usuario=perfil, nome="X", data=date(2026,1,1), local="Y", tipo="Z", estimativa_convidados="10")
        self.tarefa = Tarefa.objects.create(evento=self.evento, titulo="Teste Check", data_limite=date(2026,1,1), feito=False)

    def test_login_redireciona_admin(self):
        """Login de Admin deve redirecionar (302) para /dashboard/"""
        url = reverse('login_session')
        data = {'username': 'admin', 'password': '123'}
        
        response = self.client.post(url, data)
        
        # Agora esperamos 302 (Redirect) e não 200
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dashboard/')

    def test_login_redireciona_colaborador(self):
        """Login de Colaborador deve redirecionar para /colaborador/home/"""
        url = reverse('login_session')
        data = {'username': 'staff@teste.com', 'password': '123'}
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, 302)
        # Verifica se redirecionou para a URL que contém 'colaborador'
        self.assertIn('colaborador', response.url)

    def test_api_toggle_tarefa(self):
        """Testa se clicar no checkbox muda o status no banco"""
        self.assertFalse(self.tarefa.feito)
        
        url = reverse('toggle_tarefa', args=[self.tarefa.id])
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 200)
        self.tarefa.refresh_from_db()
        self.assertTrue(self.tarefa.feito)