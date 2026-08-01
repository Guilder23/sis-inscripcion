from django.db import models
from docentes.models import Docente


class Facultad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveIntegerField(default=4)
    semestre = models.PositiveIntegerField(default=1)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'


class Grupo(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='grupos')
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='grupos')
    horario = models.CharField(max_length=100, blank=True)
    numero = models.PositiveIntegerField()
    cupo = models.PositiveIntegerField(default=30)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.materia.codigo} - Grupo {self.numero}'
