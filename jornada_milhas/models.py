from django.db import models


class Depoimento(models.Model):
    foto = models.ImageField()
    depoimento = models.TextField()
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.depoimento


class Destino(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=50)
    preco = models.DecimalField()

    def __str__(self):
        return self.nome
