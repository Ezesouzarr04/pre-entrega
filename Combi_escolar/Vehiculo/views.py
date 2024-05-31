from django.shortcuts import render
from . import models
from Vehiculo.models import Turno

def index(request):
    consulta = models.Turno.objects.all()
    contexto = {"Turnos": consulta}
    return render(request, "Vehiculo/index.html", contexto)

def turno_list(request):
    consulta = Turno.objects.all()
    contexto = {"Turnos": consulta}
    return render(request, "Vehiculo/turno_list.html", contexto)
