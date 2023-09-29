from rest_framework import viewsets
from jornada_milhas.serializer import DepoimentoSerializer
from jornada_milhas.models import Depoimento


class DepoimentosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer
