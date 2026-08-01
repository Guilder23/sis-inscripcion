from django.shortcuts import render, redirect, get_object_or_404
from docentes.models import Docente
from .models import Facultad, Materia, Grupo


def facultades(request):
    facultades = Facultad.objects.all()
    if request.method == 'POST':
        Facultad.objects.create(nombre=request.POST.get('nombre'))
        return redirect('facultades')
    return render(request, 'academico/facultades.html', {'facultades': facultades})


def facultad_editar(request, pk):
    facultad = get_object_or_404(Facultad, pk=pk)
    if request.method == 'POST':
        facultad.nombre = request.POST.get('nombre')
        facultad.save()
        return redirect('facultades')
    return render(request, 'academico/facultad_form.html', {'facultad': facultad})


def facultad_eliminar(request, pk):
    facultad = get_object_or_404(Facultad, pk=pk)
    facultad.delete()
    return redirect('facultades')


def materias(request):
    materias = Materia.objects.select_related('facultad').all()
    facultades = Facultad.objects.all()
    if request.method == 'POST':
        Materia.objects.create(
            nombre=request.POST.get('nombre'),
            codigo=request.POST.get('codigo'),
            creditos=request.POST.get('creditos', 4),
            facultad=Facultad.objects.get(pk=request.POST.get('facultad')),
        )
        return redirect('materias')
    return render(request, 'academico/materias.html', {'materias': materias, 'facultades': facultades})


def materia_editar(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    facultades = Facultad.objects.all()
    if request.method == 'POST':
        materia.nombre = request.POST.get('nombre')
        materia.codigo = request.POST.get('codigo')
        materia.creditos = request.POST.get('creditos', 4)
        materia.facultad = Facultad.objects.get(pk=request.POST.get('facultad'))
        materia.save()
        return redirect('materias')
    return render(request, 'academico/materia_form.html', {'materia': materia, 'facultades': facultades})


def materia_eliminar(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    materia.delete()
    return redirect('materias')


def grupos(request):
    grupos = Grupo.objects.select_related('materia', 'docente').all()
    materias = Materia.objects.all()
    docentes = Docente.objects.all()
    if request.method == 'POST':
        Grupo.objects.create(
            materia=Materia.objects.get(pk=request.POST.get('materia')),
            docente=Docente.objects.get(pk=request.POST.get('docente')) if request.POST.get('docente') else None,
            horario=request.POST.get('horario', ''),
            numero=request.POST.get('numero'),
            cupo=request.POST.get('cupo', 30),
        )
        return redirect('grupos')
    return render(request, 'academico/grupos.html', {'grupos': grupos, 'materias': materias, 'docentes': docentes})


def grupo_editar(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    materias = Materia.objects.all()
    docentes = Docente.objects.all()
    if request.method == 'POST':
        grupo.materia = Materia.objects.get(pk=request.POST.get('materia'))
        grupo.docente = Docente.objects.get(pk=request.POST.get('docente')) if request.POST.get('docente') else None
        grupo.horario = request.POST.get('horario', '')
        grupo.numero = request.POST.get('numero')
        grupo.cupo = request.POST.get('cupo', 30)
        grupo.save()
        return redirect('grupos')
    return render(request, 'academico/grupo_form.html', {'grupo': grupo, 'materias': materias, 'docentes': docentes})


def grupo_eliminar(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    grupo.delete()
    return redirect('grupos')
