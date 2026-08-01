from django.shortcuts import render, redirect, get_object_or_404
from .models import Docente


def docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes/docentes.html', {'docentes': docentes})


def docente_nuevo(request):
    if request.method == 'POST':
        Docente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            ci=request.POST.get('ci'),
            especialidad=request.POST.get('especialidad'),
            activo=request.POST.get('activo') == 'on',
        )
        return redirect('docentes')
    return render(request, 'docentes/docente_form.html')


def docente_editar(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.nombre = request.POST.get('nombre')
        docente.apellido = request.POST.get('apellido')
        docente.ci = request.POST.get('ci')
        docente.especialidad = request.POST.get('especialidad')
        docente.activo = request.POST.get('activo') == 'on'
        docente.save()
        return redirect('docentes')
    return render(request, 'docentes/docente_form.html', {'docente': docente})


def docente_eliminar(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    docente.delete()
    return redirect('docentes')
