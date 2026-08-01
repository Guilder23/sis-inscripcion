from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('academico/', include('academico.urls')),
    path('estudiantes/', include('estudiantes.urls')),
    path('docentes/', include('docentes.urls')),
    path('inscripciones/', include('inscripciones.urls')),
    path('reportes/', include('reportes.urls')),
]
