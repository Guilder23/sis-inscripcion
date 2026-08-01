from django.urls import path
from .views import estudiantes, estudiante_nuevo, estudiante_editar, estudiante_eliminar

urlpatterns = [
    path('', estudiantes, name='estudiantes'),
    path('nuevo/', estudiante_nuevo, name='estudiante_nuevo'),
    path('editar/<int:pk>/', estudiante_editar, name='estudiante_editar'),
    path('eliminar/<int:pk>/', estudiante_eliminar, name='estudiante_eliminar'),
]
