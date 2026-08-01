from django.db import models
from estudiantes.models import Estudiante
from academico.models import Grupo


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='inscripciones')
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='ACTIVA')

    def __str__(self):
        return f'{self.estudiante.codigo} - {self.grupo}'
