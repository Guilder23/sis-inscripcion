from django.shortcuts import render
from inscripciones.models import Inscripcion


def historial(request):
    if request.user.is_staff:
        inscripciones = Inscripcion.objects.select_related('estudiante', 'grupo__materia').all()
    else:
        estudiante = getattr(request.user, 'estudiante', None)
        inscripciones = Inscripcion.objects.filter(estudiante=estudiante).select_related('grupo__materia') if estudiante else Inscripcion.objects.none()
    return render(request, 'reportes/historial.html', {'inscripciones': inscripciones})
