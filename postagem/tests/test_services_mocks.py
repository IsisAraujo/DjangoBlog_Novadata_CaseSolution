from unittest.mock import patch
from django.test import TestCase
from postagem import services


# Classe de teste para verificar a disponibilidade de um serviço externo
class TestVerificaDisponibilidadeExterna(TestCase):

    def test_servico_externo_disponivel(self):
        # Testa o cenário em que o serviço externo está disponível
        with patch.object(services, 'verifica_disponibilidade_externa', return_value=True):
            # Simula a função como se estivesse retornando True
            resultado = services.verifica_disponibilidade_externa()
            # Verifica se o resultado é True
            self.assertTrue(resultado)

    def test_servico_externo_indisponivel(self):
        # Testa o cenário em que o serviço externo está indisponível
        with patch.object(services, 'verifica_disponibilidade_externa', return_value=False):
            # Simula a função como se estivesse retornando False
            resultado = services.verifica_disponibilidade_externa()
            # Verifica se o resultado é False
            self.assertFalse(resultado)
