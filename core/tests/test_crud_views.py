from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Servico, Fornecedor, Evento, Usuario
from datetime import date

class CrudTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Cria e Loga como Admin (obrigatório para acessar essas views)
        self.admin = User.objects.create_user(username='admin', password='123', is_staff=True)
        self.client.login(username='admin', password='123')

    def test_criar_servico_view(self):
        """Testa se a view servico_novo realmente salva no banco"""
        url = reverse('servico_novo')
        dados = {
            'titulo': 'Assessoria Dia',
            'descricao': 'Apenas no dia',
            'preco': '2000.00'
        }
        
        # Simula o POST (clique no botão Salvar)
        response = self.client.post(url, dados)
        
        # 1. Deve redirecionar para a lista (Status 302)
        self.assertEqual(response.status_code, 302)
        
        # 2. Deve ter criado no banco
        self.assertTrue(Servico.objects.filter(titulo='Assessoria Dia').exists())

    def test_editar_fornecedor_view(self):
        """Testa se a edição atualiza os dados"""
        # Cria dados base
        cliente = Usuario.objects.create(nome="Cli", email="c@c.com", tipo="Noiva")
        evento = Evento.objects.create(usuario=cliente, nome="Festa", data=date(2026,1,1), local="X", tipo="Y", estimativa_convidados="10")
        fornecedor = Fornecedor.objects.create(evento=evento, empresa="Buffet Ruim", servico="Comida", status="Pendente")
        
        # Tenta editar
        url = reverse('fornecedor_editar', args=[fornecedor.id])
        novos_dados = {
            'evento': evento.id,
            'empresa': 'Buffet Bom', # Mudou o nome
            'servico': 'Comida Gourmet',
            'status': 'Confirmado'
        }
        
        self.client.post(url, novos_dados)
        
        # Verifica se mudou no banco
        fornecedor.refresh_from_db()
        self.assertEqual(fornecedor.empresa, 'Buffet Bom')
        self.assertEqual(fornecedor.status, 'Confirmado')