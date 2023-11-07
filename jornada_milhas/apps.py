from django.apps import AppConfig


class JornadaMilhasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jornada_milhas'

    def ready(self) -> None:
        from django.db.models.signals import pre_delete, pre_save

        from .models import Depoimento, Destino
        from .signals import image_depoimento, image_destino

        pre_delete.connect(image_depoimento, sender=Depoimento)
        pre_delete.connect(image_destino, sender=Destino)
        pre_save.connect(image_depoimento, sender=Depoimento)
        pre_save.connect(image_destino, sender=Destino)
