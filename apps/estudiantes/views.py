from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante


def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/estudiantes.html', {'estudiantes': estudiantes})


def estudiante_nuevo(request):
    if request.method == 'POST':
        Estudiante.objects.create(
            codigo=request.POST.get('codigo'),
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            carrera=request.POST.get('carrera'),
            activo=request.POST.get('activo') == 'on',
        )
        return redirect('estudiantes')
    return render(request, 'estudiantes/estudiante_form.html')


def estudiante_editar(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.codigo = request.POST.get('codigo')
        estudiante.nombre = request.POST.get('nombre')
        estudiante.apellido = request.POST.get('apellido')
        estudiante.email = request.POST.get('email')
        estudiante.carrera = request.POST.get('carrera')
        estudiante.activo = request.POST.get('activo') == 'on'
        estudiante.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/estudiante_form.html', {'estudiante': estudiante})


def estudiante_eliminar(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    estudiante.delete()
    return redirect('estudiantes')
