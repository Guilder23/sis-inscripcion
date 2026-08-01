from django.db import models


class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=100)
    facultad = models.ForeignKey('academico.Facultad', on_delete=models.SET_NULL, null=True, blank=True, related_name='docentes')
    carrera = models.ForeignKey('academico.Carrera', on_delete=models.SET_NULL, null=True, blank=True, related_name='docentes')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
