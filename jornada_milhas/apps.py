from django.apps import AppConfig


class JornadaMilhasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jornada_milhas'

    def ready(self) -> None:
        from django.db.models.signals import pre_delete, pre_save

        from .models import Depoimento
        from .signals import delete_image

        pre_delete.connect(delete_image, sender=Depoimento)
        pre_save.connect(delete_image, sender=Depoimento)
