from django.shortcuts import render
from . import models
from Vehiculo.models import Turno_de_recorrido

def index(request):
    consulta = models.Turno_de_recorrido.objects.all()
    contexto = {"Turnos": consulta}
    return render(request, "Vehiculo/index.html", contexto)

def turno_list(request):
    consulta = Turno_de_recorrido.objects.all()
    contexto = {"Turnos": consulta}
    return render(request, "Vehiculo/turno_list.html", contexto)

