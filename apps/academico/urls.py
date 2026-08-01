from django.urls import path
from .views import (
    facultades, facultad_editar, facultad_eliminar,
    carreras, carrera_editar, carrera_eliminar,
    materias, materia_editar, materia_eliminar,
    grupos, grupo_editar, grupo_eliminar,
)

urlpatterns = [
    path('facultades/', facultades, name='facultades'),
    path('facultades/editar/<int:pk>/', facultad_editar, name='facultad_editar'),
    path('facultades/eliminar/<int:pk>/', facultad_eliminar, name='facultad_eliminar'),
    path('carreras/', carreras, name='carreras'),
    path('carreras/editar/<int:pk>/', carrera_editar, name='carrera_editar'),
    path('carreras/eliminar/<int:pk>/', carrera_eliminar, name='carrera_eliminar'),
    path('materias/', materias, name='materias'),
    path('materias/editar/<int:pk>/', materia_editar, name='materia_editar'),
    path('materias/eliminar/<int:pk>/', materia_eliminar, name='materia_eliminar'),
    path('grupos/', grupos, name='grupos'),
    path('grupos/editar/<int:pk>/', grupo_editar, name='grupo_editar'),
    path('grupos/eliminar/<int:pk>/', grupo_eliminar, name='grupo_eliminar'),
]
