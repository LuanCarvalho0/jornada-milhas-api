from django.conf import settings
import os


def delete_image(sender, instance, **kwargs):
    depoimento = sender.objects.filter(id=instance.id).first()
    if depoimento:
        old_image_path = os.path.join(settings.MEDIA_ROOT, depoimento.foto.name)
        if os.path.exists(old_image_path):
            os.remove(old_image_path)
