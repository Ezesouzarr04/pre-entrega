from django.db import models


class Combi(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.nombre


class Pasajero(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre


class Conductor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre


class Turno_de_recorrido(models.Model):
    nombre = models.PositiveIntegerField(unique=True)
    combi = models.ForeignKey(Combi, on_delete=models.SET_NULL, null=True, blank=True)
    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, null=True, blank=True)
    pasajero = models.ManyToManyField(Pasajero)

    def __str__(self):
        return self.nombre