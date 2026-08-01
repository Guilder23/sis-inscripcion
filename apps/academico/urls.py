from django.urls import path
from .views import facultades, materias, grupos

urlpatterns = [
    path('facultades/', facultades, name='facultades'),
    path('materias/', materias, name='materias'),
    path('grupos/', grupos, name='grupos'),
]
