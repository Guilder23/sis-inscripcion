from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from estudiantes.models import Estudiante
from inscripciones.models import Inscripcion


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if getattr(user, 'is_staff', False):
                return redirect('dashboard')
            return redirect('student_dashboard')
        return render(request, 'accounts/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    stats = {
        'estudiantes': Estudiante.objects.count(),
        'inscripciones': Inscripcion.objects.count(),
    }
    return render(request, 'dashboard.html', {'stats': stats})


@login_required
def student_dashboard(request):
    estudiante = request.user.estudiante if hasattr(request.user, 'estudiante') else None
    inscripciones = Inscripcion.objects.filter(estudiante=estudiante).select_related('grupo__materia', 'grupo__docente') if estudiante else []
    return render(request, 'accounts/student_dashboard.html', {'estudiante': estudiante, 'inscripciones': inscripciones})
