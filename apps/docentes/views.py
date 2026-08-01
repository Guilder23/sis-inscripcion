from django.shortcuts import render, redirect, get_object_or_404
from academico.models import Facultad, Carrera
from .models import Docente


def docentes(request):
    docentes = Docente.objects.select_related('facultad', 'carrera').all()
    return render(request, 'docentes/docentes.html', {'docentes': docentes})


def docente_nuevo(request):
    facultades = Facultad.objects.all()
    carreras = Carrera.objects.select_related('facultad').all()
    if request.method == 'POST':
        Docente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            ci=request.POST.get('ci'),
            especialidad=request.POST.get('especialidad'),
            facultad=Facultad.objects.get(pk=request.POST.get('facultad')) if request.POST.get('facultad') else None,
            carrera=Carrera.objects.get(pk=request.POST.get('carrera')) if request.POST.get('carrera') else None,
            activo=request.POST.get('activo') == 'on',
        )
        return redirect('docentes')
    return render(request, 'docentes/docente_form.html', {'facultades': facultades, 'carreras': carreras})


def docente_editar(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    facultades = Facultad.objects.all()
    carreras = Carrera.objects.select_related('facultad').all()
    if request.method == 'POST':
        docente.nombre = request.POST.get('nombre')
        docente.apellido = request.POST.get('apellido')
        docente.ci = request.POST.get('ci')
        docente.especialidad = request.POST.get('especialidad')
        docente.facultad = Facultad.objects.get(pk=request.POST.get('facultad')) if request.POST.get('facultad') else None
        docente.carrera = Carrera.objects.get(pk=request.POST.get('carrera')) if request.POST.get('carrera') else None
        docente.activo = request.POST.get('activo') == 'on'
        docente.save()
        return redirect('docentes')
    return render(request, 'docentes/docente_form.html', {'docente': docente, 'facultades': facultades, 'carreras': carreras})


def docente_eliminar(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    docente.delete()
    return redirect('docentes')
