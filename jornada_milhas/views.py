from rest_framework import viewsets
from jornada_milhas.serializer import DepoimentoSerializer
from jornada_milhas.models import Depoimento


class DepoimentosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer
    http_method_names = ['get','post', 'put', 'delete']


class DepoimentosHomeViewSet(viewsets.ModelViewSet):
    """Exibir 3 depoimentos Aleatório"""
    queryset = Depoimento.objects.order_by('?')[:3]
    serializer_class = DepoimentoSerializer
    http_method_names = ['get']
