from rest_framework import viewsets, status, generics
from jornada_milhas.serializer import DepoimentoSerializer, DestinoSerializer
from jornada_milhas.models import Depoimento, Destino
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class DepoimentosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer
    http_method_names = ['get','post', 'put', 'delete']


class DepoimentosHomeViewSet(generics.ListAPIView):
    """Exibir 3 depoimentos Aleatório"""
    def get_queryset(self):
        queryset = Depoimento.objects.order_by('?')[:3]
        return queryset
    serializer_class = DepoimentoSerializer
   

class DestinosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os destinos"""  
    serializer_class = DestinoSerializer
    http_method_names = ['get','post', 'put', 'delete']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Destino.objects.all()
        nome = self.request.query_params.get('nome')
        if nome is not None:
            queryset = queryset.filter(Q(nome__icontains=nome))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response({"mensagem": "Nenhum destino foi encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
