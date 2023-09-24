from django.db import models
import os

class Depoimento(models.Model):
    foto = models.ImageField()
    depoimento = models.TextField()
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.depoimento

    def remove_foto(self):
        if os.path.isfile(self.foto.path):
            os.remove(self.foto.path)
