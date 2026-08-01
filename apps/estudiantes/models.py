from django.db import models
from django.contrib.auth.models import User


class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='estudiante', null=True, blank=True)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    facultad = models.ForeignKey('academico.Facultad', on_delete=models.SET_NULL, null=True, blank=True, related_name='estudiantes')
    carrera = models.ForeignKey('academico.Carrera', on_delete=models.SET_NULL, null=True, blank=True, related_name='estudiantes')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.codigo} - {self.nombre} {self.apellido}'
