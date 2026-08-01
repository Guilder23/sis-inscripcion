from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from academico.models import Grupo, Materia
from estudiantes.models import Estudiante
from .models import Inscripcion


@login_required
def inscripciones(request):
    if request.user.is_staff:
        inscripciones = Inscripcion.objects.select_related('estudiante', 'grupo__materia').all()
        return render(request, 'inscripciones/inscripciones.html', {'inscripciones': inscripciones})

    estudiante = request.user.estudiante
    inscripciones = Inscripcion.objects.filter(estudiante=estudiante).select_related('grupo__materia', 'grupo__docente')
    materias = Materia.objects.select_related('facultad').prefetch_related('grupos__docente').all()
    if estudiante and estudiante.carrera:
        materias = materias.filter(facultad__nombre=estudiante.carrera)
    else:
        materias = Materia.objects.none()
    return render(request, 'inscripciones/inscripciones.html', {
        'inscripciones': inscripciones,
        'estudiante': estudiante,
        'materias': materias,
    })


@login_required
def nueva_inscripcion(request):
    estudiante = request.user.estudiante if hasattr(request.user, 'estudiante') else None
    if request.method == 'POST':
        if estudiante is None:
            return redirect('student_dashboard')
        grupo = Grupo.objects.get(pk=request.POST.get('grupo'))
        grupos_disponibles = Grupo.objects.filter(activo=True, materia__facultad__nombre=estudiante.carrera).select_related('materia', 'docente').all() if estudiante.carrera else Grupo.objects.none()
        if Inscripcion.objects.filter(estudiante=estudiante, grupo=grupo).exists():
            return render(request, 'inscripciones/inscripcion_form.html', {'error': 'Ya estás inscrito en este grupo.', 'grupos': grupos_disponibles})
        if Inscripcion.objects.filter(grupo=grupo).count() >= grupo.cupo:
            return render(request, 'inscripciones/inscripcion_form.html', {'error': 'El grupo ya alcanzó su cupo.', 'grupos': grupos_disponibles})
        Inscripcion.objects.create(estudiante=estudiante, grupo=grupo)
        return redirect('student_dashboard')
    grupos = Grupo.objects.filter(activo=True).select_related('materia', 'docente').all()
    if estudiante and estudiante.carrera:
        grupos = grupos.filter(materia__facultad__nombre=estudiante.carrera)
    else:
        grupos = Grupo.objects.none()
    return render(request, 'inscripciones/inscripcion_form.html', {'grupos': grupos, 'estudiante': estudiante})
