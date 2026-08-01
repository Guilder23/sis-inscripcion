from django.shortcuts import render
from inscripciones.models import Inscripcion


def historial(request):
    inscripciones = Inscripcion.objects.select_related('estudiante', 'grupo__materia').all()
    return render(request, 'reportes/historial.html', {'inscripciones': inscripciones})
