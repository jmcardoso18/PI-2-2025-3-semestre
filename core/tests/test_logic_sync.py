from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Usuario

class UserSyncTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_user(username='admin', password='123', is_staff=True)
        self.client.login(username='admin', password='123')

    def test_criacao_automatica_login(self):
        """
        Ao criar um cliente via Dashboard, o sistema deve criar 
        automaticamente um User do Django para ele logar.
        """
        url = reverse('cliente_novo')
        dados = {
            'nome': 'Cliente Sincronizado',
            'email': 'sync@teste.com', # Esse será o login
            'senha': 'senha_secreta_123',
            'tipo': 'Noiva',
            'celular': '1199999999'
        }
        
        # Envia o formulário
        self.client.post(url, dados)
        
        # VERIFICAÇÃO 1: Criou na tabela do negócio?
        self.assertTrue(Usuario.objects.filter(email='sync@teste.com').exists())
        
        # VERIFICAÇÃO 2: Criou na tabela de autenticação (auth_user)?
        login_criado = User.objects.filter(username='sync@teste.com').exists()
        self.assertTrue(login_criado, "FALHA CRÍTICA: O login do Django não foi criado automaticamente!")
        
        # VERIFICAÇÃO 3: A senha funciona?
        user = User.objects.get(username='sync@teste.com')
        self.assertTrue(user.check_password('senha_secreta_123'))