from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from estudiantes.models import Estudiante
from academico.models import Grupo
from .models import Inscripcion


@login_required
def inscripciones(request):
    if request.user.is_staff:
        inscripciones = Inscripcion.objects.select_related('estudiante', 'grupo__materia').all()
        return render(request, 'inscripciones/inscripciones.html', {'inscripciones': inscripciones})

    estudiante = request.user.estudiante
    inscripciones = Inscripcion.objects.filter(estudiante=estudiante).select_related('grupo__materia', 'grupo__docente')
    return render(request, 'inscripciones/inscripciones.html', {'inscripciones': inscripciones, 'estudiante': estudiante})


@login_required
def nueva_inscripcion(request):
    estudiante = request.user.estudiante if hasattr(request.user, 'estudiante') else None
    if request.method == 'POST':
        if estudiante is None:
            return redirect('student_dashboard')
        grupo = Grupo.objects.get(pk=request.POST.get('grupo'))
        if Inscripcion.objects.filter(estudiante=estudiante, grupo=grupo).exists():
            return render(request, 'inscripciones/inscripcion_form.html', {'error': 'Ya estás inscrito en este grupo.', 'grupos': Grupo.objects.select_related('materia', 'docente').all()})
        if Inscripcion.objects.filter(grupo=grupo).count() >= grupo.cupo:
            return render(request, 'inscripciones/inscripcion_form.html', {'error': 'El grupo ya alcanzó su cupo.', 'grupos': Grupo.objects.select_related('materia', 'docente').all()})
        Inscripcion.objects.create(estudiante=estudiante, grupo=grupo)
        return redirect('student_dashboard')
    grupos = Grupo.objects.select_related('materia', 'docente').all()
    return render(request, 'inscripciones/inscripcion_form.html', {'grupos': grupos, 'estudiante': estudiante})
