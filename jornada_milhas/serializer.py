from rest_framework import serializers
from jornada_milhas.models import Depoimento
import os


class DepoimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Depoimento
        fields = '__all__'

    def update(self, instance, validated_data):
        if instance.foto:

            old_image_path = instance.foto.path

            if os.path.exists(old_image_path):
                os.remove(old_image_path)

        instance.nome = validated_data.get('nome', instance.nome)
        instance.depoimento = validated_data.get('depoimento', instance.depoimento)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.save()

        return instance