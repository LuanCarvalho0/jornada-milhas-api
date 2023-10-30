from rest_framework.test import APITestCase
from jornada_milhas.models import Depoimento
from django.urls import reverse
from rest_framework import status
from .utils import valid_image, delete_image_test


class DepoimentosTestCase(APITestCase):

    def setUp(self) -> None:
        self.list_url = reverse('Depoimentos-list')

        self.depoimento_1 = Depoimento.objects.create(
            foto = 'image.jpg',
            depoimento = 'Este é um depoimento de teste',
            nome = 'João Silva'
        )
        self.depoimento_2 = Depoimento.objects.create(
            foto = 'image2.jpg',
            depoimento = 'Este é um depoimento de teste 2',
            nome = 'Maria Souza'
        )
    
    def test_requisicao_get_para_listar_todos_os_depoimentos(self) -> None:
        """Teste para verificar a requisição GET para listar os depoimentos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_um_depoimento(self) -> None:
        """Teste para verificar a requisição POST para criar um depoimento"""
        foto = valid_image()
        data = {
            'foto': foto,
            'depoimento': 'Este é um depoimento de teste 3',
            'nome': 'Daniel Bas'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        delete_image_test('depoimentos/')

    def test_requisicao_delete_para_deletar_depoimento(self) -> None:
        """Teste para verificar a requisição DELETE para deletar um depoimento"""
        response = self.client.delete('/depoimentos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_depoimento(self) -> None:
        """Teste para verificar requisição PUT para atualizar um depoimento"""
        foto = valid_image()
        data = {
            'foto': foto,
            'depoimento': 'Este é um depoimento de teste atualizado',
            'nome': 'João Victor '
        }
        response = self.client.put('/depoimentos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        delete_image_test('depoimentos/')
