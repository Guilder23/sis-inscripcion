from django.urls import path
from .views import inscripciones, nueva_inscripcion

urlpatterns = [
    path('', inscripciones, name='inscripciones'),
    path('nueva/', nueva_inscripcion, name='nueva_inscripcion'),
]
