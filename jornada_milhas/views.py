from rest_framework import viewsets, status
from jornada_milhas.serializer import DepoimentoSerializer
from jornada_milhas.models import Depoimento
from rest_framework.response import Response


class DepoimentosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer

    def update(self, request, pk):
        try:
            db_depoimento = self.get_object()
            data = request.data
        except:
            return Response({"msg": "depoimento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        db_depoimento.remove_foto()
        db_depoimento.foto = data["foto"]
        db_depoimento.depoimento = data["depoimento"]
        db_depoimento.nome = data["nome"]
        db_depoimento.save()
        serializer = DepoimentoSerializer(db_depoimento)

        return Response(serializer.data, status=status.HTTP_200_OK)
