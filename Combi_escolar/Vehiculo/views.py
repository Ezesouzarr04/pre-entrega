from django.shortcuts import render

from . import models

def index(request):
    consulta = models.Turno_de_recorrido.objects.all()
    contexto = {"TurnosDeRecorridos": consulta}
    return render(request, "Vehiculo/index.html", contexto)