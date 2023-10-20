from rest_framework import viewsets
from jornada_milhas.serializer import DepoimentoSerializer, DestinoSerializer
from jornada_milhas.models import Depoimento, Destino


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


class DestinosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os destinos"""  
    serializer_class = DestinoSerializer
    http_method_names = ['get','post', 'put', 'delete']

    def get_queryset(self):
        
        queryset = Destino.objects.all()
        nome = self.request.query_params.get('nome')
        if nome is not None:
            queryset = queryset.filter(nome=nome)
        return queryset
