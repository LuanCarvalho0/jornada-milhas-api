from rest_framework.test import APITestCase
from jornada_milhas.models import Destino
from django.urls import reverse
from rest_framework import status
from .utils import valid_image, delete_image_test


class DestinosTestCase(APITestCase):

    def setUp(self) -> None:
        self.list_url = reverse('Destinos-list')

        self.destino_1 = Destino.objects.create(
            foto = 'image.jpg',
            nome = 'Maldivas',
            preco = 20000
        )
        self.destino_2 = Destino.objects.create(
            foto = 'teste2.jpg',
            nome = 'Nova York',
            preco = 12000
        )
    
    def test_requisicao_get_para_listar_todos_os_destinos(self) -> None:
        """Teste para verificar a requisição GET para listar os destinos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_um_destino(self) -> None:
        """Teste para verificar a requisição POST para criar um destino"""
        foto = valid_image()
        data = {
            'foto': foto,
            'nome': 'Moscou',
            'preco': 15000
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        delete_image_test('destinos/')

    def test_requisicao_delete_para_deletar_destino(self) -> None:
        """Teste para verificar a requisição DELETE para deletar um destino"""
        response = self.client.delete('/destinos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_destino(self) -> None:
        """Teste para verificar requisição PUT para atualizar um destino"""
        foto = valid_image()
        data = {
            'foto': foto,
            'nome': 'Maldivas',
            'preco': 25000
        }
        response = self.client.put('/destinos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        delete_image_test('destinos/')
