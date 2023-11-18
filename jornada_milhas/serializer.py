from rest_framework import serializers
from jornada_milhas.models import Depoimento, Destino
from openai_api.chat_gpt import get_texto_descritivo 

class DepoimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Depoimento
        fields = ('id', 'foto', 'depoimento', 'nome')


class DestinoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destino
        fields = '__all__'

    def validate(self, data):
        if data['texto_descritivo'] == "":
            data['texto_descritivo'] = get_texto_descritivo(data['nome'])
        return data
