from django.db import models


class Facultad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveIntegerField(default=4)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'


class Grupo(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='grupos')
    numero = models.PositiveIntegerField()
    cupo = models.PositiveIntegerField(default=30)

    def __str__(self):
        return f'{self.materia.codigo} - Grupo {self.numero}'
