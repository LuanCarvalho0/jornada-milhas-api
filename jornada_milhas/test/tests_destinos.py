from rest_framework.test import APITestCase
from jornada_milhas.models import Destino
from django.urls import reverse
from rest_framework import status
from .utils import valid_image, delete_image_test


class DestinosTestCase(APITestCase):

    def setUp(self) -> None:
        self.list_url = reverse('Destinos-list')

        self.destino_1 = Destino.objects.create(
            foto_1 = 'image1.jpg',
            foto_2 = 'image2.jpg',
            nome = 'Maldivas',
            meta = 'Meta teste',
            preco = 20000,
            texto_descritivo = "Texto teste"
        )
        self.destino_2 = Destino.objects.create(
            foto_1 = 'teste1.jpg',
            foto_2 = 'teste2.jpg',
            nome = 'Nova York',
            meta = 'Meta teste',
            preco = 12000,
            texto_descritivo = "Texo teste"
        )
    
    def test_requisicao_get_para_listar_todos_os_destinos(self) -> None:
        """Teste para verificar a requisição GET para listar os destinos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_um_destino(self) -> None:
        """Teste para verificar a requisição POST para criar um destino"""
        foto_1 = valid_image('test-image1.png')
        foto_2 = valid_image('test-image2.png')
        data = {
            'foto_1': foto_1,
            'foto_2': foto_2,
            'nome': 'Moscou',
            'meta': 'Meta Teste',
            'preco': 15000,
            'texto_descritivo': 'Texto teste'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        delete_image_test(f'destinos/{foto_1.name}')
        delete_image_test(f'destinos/{foto_2.name}')

    def test_requisicao_delete_para_deletar_destino(self) -> None:
        """Teste para verificar a requisição DELETE para deletar um destino"""
        response = self.client.delete('/destinos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_destino(self) -> None:
        """Teste para verificar requisição PUT para atualizar um destino"""
        foto_1 = valid_image('test-image1.png')
        foto_2 = valid_image('test-image2.png')
        data = {
            'foto_1': foto_1,
            'foto_2': foto_2,
            'nome': 'Maldivas',
            'meta': 'Meta Teste',
            'preco': 36000,
            'texto_descritivo': 'Texto teste'
        }
        response = self.client.put('/destinos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        delete_image_test(f'destinos/{foto_1.name}')
        delete_image_test(f'destinos/{foto_2.name}')
