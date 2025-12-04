from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Usuario, Evento, Servico
from datetime import date

class BusinessRulesTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # 1. Cria Admin
        self.admin_user = User.objects.create_user(username='admin', email='admin@teste.com', password='123', is_staff=True)
        
        # 2. Cria Cliente A (Noiva 1)
        self.user_a = User.objects.create_user(username='a@teste.com', email='a@teste.com', password='123')
        self.perfil_a = Usuario.objects.create(nome="Noiva A", email="a@teste.com", tipo="Noiva")
        self.evento_a = Evento.objects.create(usuario=self.perfil_a, nome="Casamento A", data=date(2026,1,1), local="Local A", tipo="Casamento", estimativa_convidados="100")

        # 3. Cria Cliente B (Noiva 2)
        self.user_b = User.objects.create_user(username='b@teste.com', email='b@teste.com', password='123')
        self.perfil_b = Usuario.objects.create(nome="Noiva B", email="b@teste.com", tipo="Noiva")
        self.evento_b = Evento.objects.create(usuario=self.perfil_b, nome="Casamento B", data=date(2026,2,2), local="Local B", tipo="Casamento", estimativa_convidados="200")

        # 4. Cria Colaborador
        self.user_colab = User.objects.create_user(username='staff@teste.com', email='staff@teste.com', password='123')
        self.perfil_colab = Usuario.objects.create(nome="Staff", email="staff@teste.com", tipo="Colaborador")

    # TESTE 16: Contagem dos KPIs do Dashboard
    def test_dashboard_kpis_contagem(self):
        """Verifica se o Dashboard está contando corretamente o total de eventos e clientes"""
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse('dashboard'))
        
        # Temos 2 eventos e 3 usuários (perfis) criados no setUp
        self.assertEqual(response.context['total_eventos'], 2)
        self.assertEqual(response.context['total_clientes'], 3)

    # TESTE 17: Isolamento de Dados (Cliente A não vê Cliente B)
    def test_isolamento_dados_cliente(self):
        """A Noiva A deve ver APENAS o seu evento, e não o da Noiva B"""
        self.client.login(username='a@teste.com', password='123')
        response = self.client.get(reverse('area_cliente'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Casamento A")
        self.assertNotContains(response, "Casamento B") # Segurança Crítica!

    # TESTE 18: Fluxo do Colaborador
    def test_fluxo_colaborador(self):
        """Colaborador deve ser bloqueado no Dashboard Admin e redirecionado para sua Home"""
        self.client.login(username='staff@teste.com', password='123')
        
        # Tenta acessar o dashboard administrativo
        response = self.client.get(reverse('dashboard'))
        
        # Deve ser redirecionado (302) para a home do colaborador
        self.assertEqual(response.status_code, 302)
        self.assertIn('colaborador/home', response.url)

    # TESTE 19: Proteção de Rotas CRUD (Segurança)
    def test_protecao_crud_admin(self):
        """Um usuário comum não pode acessar a URL de criar cliente na força bruta"""
        self.client.login(username='a@teste.com', password='123') # Loga como cliente
        
        # Tenta acessar a tela de criar novo cliente
        response = self.client.get(reverse('cliente_novo'))
        
        # Deve ser bloqueado/redirecionado (302)
        self.assertEqual(response.status_code, 302)
        # O decorador @user_passes_test manda para a area-cliente se falhar
        self.assertTrue("area-cliente" in response.url)

    # TESTE 20: API Pública de Serviços (JSON)
    def test_api_servicos_json(self):
        """A API deve retornar os serviços em formato JSON correto para o React"""
        Servico.objects.create(titulo="Pacote Teste", descricao="Desc", preco=1000.00)
        
        response = self.client.get(reverse('api_servicos'))
        
        self.assertEqual(response.status_code, 200)
        dados = response.json()
        
        self.assertTrue(len(dados) > 0)
        self.assertEqual(dados[0]['titulo'], "Pacote Teste")
        self.assertEqual(dados[0]['preco'], "1000.00") # Decimal vem como string ou float dependendo do serializer