from django.shortcuts import render, redirect, get_object_or_404
from .models import Facultad, Materia, Grupo


def facultades(request):
    facultades = Facultad.objects.all()
    return render(request, 'academico/facultades.html', {'facultades': facultades})


def materias(request):
    materias = Materia.objects.select_related('facultad').all()
    return render(request, 'academico/materias.html', {'materias': materias})


def grupos(request):
    grupos = Grupo.objects.select_related('materia').all()
    return render(request, 'academico/grupos.html', {'grupos': grupos})
