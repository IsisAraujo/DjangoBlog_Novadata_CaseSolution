from unittest.mock import patch
from django.test import TestCase
from postagem import services


class TestVerificaDisponibilidadeExterna(TestCase):

    def test_servico_externo_disponivel(self):
        with patch.object(services, 'verifica_disponibilidade_externa', return_value=True):
            resultado = services.verifica_disponibilidade_externa()
            self.assertTrue(resultado)

    def test_servico_externo_indisponivel(self):
        with patch.object(services, 'verifica_disponibilidade_externa', return_value=False):
            resultado = services.verifica_disponibilidade_externa()
            self.assertFalse(resultado)
