from django.db import models


class Depoimento(models.Model):
    foto = models.ImageField(upload_to='depoimentos/')
    depoimento = models.TextField()
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.depoimento


class Destino(models.Model):
    foto_1 = models.ImageField(upload_to='destinos/')
    foto_2 = models.ImageField(upload_to='destinos/')
    nome = models.CharField(max_length=50)
    meta = models.CharField(max_length=160)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    texto_descritivo = models.TextField(max_length=210, blank=True)

    def __str__(self) -> str:
        return self.nome
