from django.test import TestCase
from core.forms import ClienteForm, ServicoForm, EventoForm
from datetime import date

class FormsTest(TestCase):
    
    def test_cliente_form_email_invalido(self):
        """O formulário deve rejeitar um email sem @ ou incompleto"""
        form = ClienteForm(data={
            'nome': 'Teste',
            'email': 'email_ruim_sem_arroba', # Inválido
            'senha': '123',
            'tipo': 'Noiva'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_servico_form_valido(self):
        """Testa se o formulário aceita dados corretos"""
        form = ServicoForm(data={
            'titulo': 'Pacote Gold',
            'descricao': 'Tudo incluso',
            'preco': '5000.00'
        })
        self.assertTrue(form.is_valid())

    def test_evento_form_obrigatorios(self):
        """Testa se o formulário reclama se faltar a data"""
        form = EventoForm(data={
            'nome': 'Casamento Sem Data',
            'local': 'Salão X'
            # Faltou 'data', 'usuario', etc
        })
        self.assertFalse(form.is_valid())
        self.assertIn('data', form.errors)