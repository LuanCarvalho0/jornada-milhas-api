from rest_framework import viewsets, status
from jornada_milhas.serializer import DepoimentoSerializer
from jornada_milhas.models import Depoimento
from rest_framework.response import Response


class DepoimentosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer
    
    def update(self, request, *args, **kwargs):
        db_depoimento = self.get_object()
        if not db_depoimento == None:
            db_depoimento.remove_foto()

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        db_depoimento = self.get_object()
        if not db_depoimento == None:
            db_depoimento.remove_foto()
        
        return super().destroy(request, *args, **kwargs)
