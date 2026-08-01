from django.urls import path
from .views import cardex, historial

urlpatterns = [
    path('', historial, name='historial'),
    path('cardex/', cardex, name='cardex'),
]
