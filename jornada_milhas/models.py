from django.db import models


class Depoimento(models.Model):
    foto = models.ImageField(upload_to='depoimentos/')
    depoimento = models.TextField()
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.depoimento


class Destino(models.Model):
    foto = models.ImageField(upload_to='destinos/')
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome
