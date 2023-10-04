from rest_framework import serializers
from jornada_milhas.models import Depoimento
import os


class DepoimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Depoimento
        fields = '__all__'
