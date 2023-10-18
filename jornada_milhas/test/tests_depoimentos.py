from rest_framework.test import APITestCase
from io import BytesIO
from jornada_milhas.models import Depoimento
from PIL import Image
import os
from django.urls import reverse
from rest_framework import status
from django.conf import settings


MEDIA_TEST =os.path.join(os.path.dirname(__file__), 'media')


class DepoimentosTestCase(APITestCase):

    def setUp(self) -> None:
        self.list_url = reverse('Depoimentos-list')

        self.depoimento_1 = Depoimento.objects.create(
            foto = 'teste.jpg',
            depoimento = 'Este é um depoimento de teste',
            nome = 'Nome do Autor'
        )
        self.depoimento_2 = Depoimento.objects.create(
            foto = 'teste2.jpg',
            depoimento = 'Este é um depoimento de teste 2',
            nome = 'Nome do Autor 2'
        )

    def valid_image(self) -> None:
        image_file = BytesIO()
        image = Image.open(os.path.join(MEDIA_TEST, 'test-image.jpg')) 
        image.save(image_file, format="PNG")
        image_file.name = 'test-image.png'
        image_file.seek(0)
        return image_file
    
    def delete_image_test(self) -> None:
        image_path = os.path.join(settings.MEDIA_ROOT, 'depoimentos/test-image.png')
        if os.path.exists(image_path):
            os.remove(image_path)
    
    def test_requisicao_get_para_listar_todos_os_depoimentos(self) -> None:
        """Teste para verificar a requisição GET para listar os depoimentos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_um_depoimento(self) -> None:
        """Teste para verificar a requisição POST para criar um depoimento"""
        foto = self.valid_image()
        data = {
            'foto': foto,
            'depoimento': 'Este é um depoimento de teste 3',
            'nome': 'Nome do Autor 3'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.delete_image_test()

    def test_requisicao_delete_para_deletar_depoimento(self) -> None:
        """Teste para verificar a requisição delete para DELETE um depoimento"""
        response = self.client.delete('/depoimentos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_depoimento(self) -> None:
        """Teste para verificar requisição PUT para atualizar um depoimento"""
        foto = self.valid_image()
        data = {
            'foto': foto,
            'depoimento': 'Este é um depoimento de teste atualizado',
            'nome': 'Nome do Autor atualizado'
        }
        response = self.client.put('/depoimentos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.delete_image_test()
