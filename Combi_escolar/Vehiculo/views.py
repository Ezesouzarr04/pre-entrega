from django.shortcuts import render

from .models import Turno_de_recorrido

def index(request):
    consulta = Turno_de_recorrido.objects.all()
    contexto = {"turnos": consulta}
    return render(request, "Vehiculo/index.html", contexto)

def turno_list(request):
    consulta = Turno_de_recorrido.objects.all()
    contexto = {"turnos": consulta}
    return render(request, "Vehiculo/turno_list.html", contexto)

