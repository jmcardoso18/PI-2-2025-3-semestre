from django.test import TestCase
from core.models import Usuario, Evento, Tarefa
from datetime import date

class ModelTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nome="Noiva Teste", 
            email="noiva@teste.com", 
            tipo="Noiva"
        )
        self.evento = Evento.objects.create(
            usuario=self.usuario,
            nome="Casamento Teste",
            data=date(2026, 12, 25),
            local="Igreja Matriz",
            tipo="Casamento",
            estimativa_convidados="200"
        )

    def test_evento_criacao(self):
        """Testa se o evento foi criado vinculado ao usuário"""
        self.assertEqual(self.evento.usuario.nome, "Noiva Teste")
        # CORREÇÃO: Usar Evento em vez de Event
        self.assertEqual(Evento.objects.count(), 1)

    def test_evento_str(self):
        esperado = "Casamento Teste (25/12/2026)"
        self.assertEqual(str(self.evento), esperado)