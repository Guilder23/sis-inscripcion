from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from academico.models import Facultad, Carrera
from .models import Estudiante


def estudiantes(request):
    estudiantes = Estudiante.objects.select_related('facultad', 'carrera').all()
    return render(request, 'estudiantes/estudiantes.html', {'estudiantes': estudiantes})


def _build_unique_username(base_username):
    username = base_username.strip()[:150]
    if not username:
        username = 'usuario'
    original = username
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f'{original}{counter}'
        counter += 1
    return username


def estudiante_nuevo(request):
    facultades = Facultad.objects.all()
    carreras = Carrera.objects.select_related('facultad').all()
    if request.method == 'POST':
        raw_username = request.POST.get('usuario') or request.POST.get('codigo') or request.POST.get('email') or 'usuario'
        username = _build_unique_username(raw_username)
        password = request.POST.get('password') or '12345678'
        user = User.objects.create_user(username=username, password=password, email=request.POST.get('email'))
        estudiante = Estudiante.objects.create(
            user=user,
            codigo=request.POST.get('codigo'),
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            facultad=Facultad.objects.get(pk=request.POST.get('facultad')) if request.POST.get('facultad') else None,
            carrera=Carrera.objects.get(pk=request.POST.get('carrera')) if request.POST.get('carrera') else None,
            activo=request.POST.get('activo') == 'on',
        )
        return redirect('estudiantes')
    return render(request, 'estudiantes/estudiante_form.html', {'facultades': facultades, 'carreras': carreras})


def estudiante_editar(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    facultades = Facultad.objects.all()
    carreras = Carrera.objects.select_related('facultad').all()
    if request.method == 'POST':
        estudiante.codigo = request.POST.get('codigo')
        estudiante.nombre = request.POST.get('nombre')
        estudiante.apellido = request.POST.get('apellido')
        estudiante.email = request.POST.get('email')
        estudiante.facultad = Facultad.objects.get(pk=request.POST.get('facultad')) if request.POST.get('facultad') else None
        estudiante.carrera = Carrera.objects.get(pk=request.POST.get('carrera')) if request.POST.get('carrera') else None
        estudiante.activo = request.POST.get('activo') == 'on'
        if estudiante.user is None:
            raw_username = request.POST.get('usuario') or request.POST.get('codigo') or request.POST.get('email') or 'usuario'
            username = _build_unique_username(raw_username)
            password = request.POST.get('password') or '12345678'
            user = User.objects.create_user(username=username, password=password, email=estudiante.email)
            estudiante.user = user
        else:
            if request.POST.get('password'):
                estudiante.user.set_password(request.POST.get('password'))
                estudiante.user.save()
        estudiante.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/estudiante_form.html', {'estudiante': estudiante, 'facultades': facultades, 'carreras': carreras})


def estudiante_eliminar(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if estudiante.user:
        estudiante.user.delete()
    estudiante.delete()
    return redirect('estudiantes')
