from django.conf import settings
import os


def delete_image(foto):
    old_image_path = os.path.join(settings.MEDIA_ROOT, foto)
    if os.path.exists(old_image_path):
        os.remove(old_image_path)

def image_depoimento(sender, instance, **kwargs):
    depoimento = sender.objects.filter(id=instance.id).first()
    if depoimento:
        delete_image(depoimento.foto.name)

def image_destino(sender, instance, **kwargs):
    destino = sender.objects.filter(id=instance.id).first()
    if destino:
        delete_image(destino.foto_1.name)
        delete_image(destino.foto_2.name)
