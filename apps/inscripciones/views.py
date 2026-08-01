from django.shortcuts import render, redirect
from estudiantes.models import Estudiante
from academico.models import Grupo
from .models import Inscripcion


def inscripciones(request):
    inscripciones = Inscripcion.objects.select_related('estudiante', 'grupo__materia').all()
    return render(request, 'inscripciones/inscripciones.html', {'inscripciones': inscripciones})


def nueva_inscripcion(request):
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(pk=request.POST.get('estudiante'))
        grupo = Grupo.objects.get(pk=request.POST.get('grupo'))
        Inscripcion.objects.create(estudiante=estudiante, grupo=grupo)
        return redirect('inscripciones')
    estudiantes = Estudiante.objects.all()
    grupos = Grupo.objects.select_related('materia').all()
    return render(request, 'inscripciones/inscripcion_form.html', {'estudiantes': estudiantes, 'grupos': grupos})
