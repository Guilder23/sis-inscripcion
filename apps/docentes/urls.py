from django.urls import path
from .views import docentes, docente_nuevo, docente_editar, docente_eliminar

urlpatterns = [
    path('', docentes, name='docentes'),
    path('nuevo/', docente_nuevo, name='docente_nuevo'),
    path('editar/<int:pk>/', docente_editar, name='docente_editar'),
    path('eliminar/<int:pk>/', docente_eliminar, name='docente_eliminar'),
]
