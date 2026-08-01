from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from academico.models import Facultad
from .models import Estudiante


def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/estudiantes.html', {'estudiantes': estudiantes})


def estudiante_nuevo(request):
    facultades = Facultad.objects.all()
    if request.method == 'POST':
        username = request.POST.get('usuario') or request.POST.get('codigo')
        password = request.POST.get('password') or '12345678'
        user = User.objects.create_user(username=username, password=password, email=request.POST.get('email'))
        estudiante = Estudiante.objects.create(
            user=user,
            codigo=request.POST.get('codigo'),
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            carrera=request.POST.get('carrera'),
            activo=request.POST.get('activo') == 'on',
        )
        return redirect('estudiantes')
    return render(request, 'estudiantes/estudiante_form.html', {'facultades': facultades})


def estudiante_editar(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    facultades = Facultad.objects.all()
    if request.method == 'POST':
        estudiante.codigo = request.POST.get('codigo')
        estudiante.nombre = request.POST.get('nombre')
        estudiante.apellido = request.POST.get('apellido')
        estudiante.email = request.POST.get('email')
        estudiante.carrera = request.POST.get('carrera')
        estudiante.activo = request.POST.get('activo') == 'on'
        if estudiante.user is None:
            username = request.POST.get('usuario') or request.POST.get('codigo')
            password = request.POST.get('password') or '12345678'
            user = User.objects.create_user(username=username, password=password, email=estudiante.email)
            estudiante.user = user
        else:
            if request.POST.get('password'):
                estudiante.user.set_password(request.POST.get('password'))
                estudiante.user.save()
        estudiante.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/estudiante_form.html', {'estudiante': estudiante, 'facultades': facultades})


def estudiante_eliminar(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if estudiante.user:
        estudiante.user.delete()
    estudiante.delete()
    return redirect('estudiantes')
