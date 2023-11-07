from rest_framework import serializers
from jornada_milhas.models import Depoimento, Destino


class DepoimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Depoimento
        fields = ('foto', 'depoimento', 'nome')


class DestinoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destino
        fields = '__all__'
