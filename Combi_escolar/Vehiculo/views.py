from django.shortcuts import render, redirect
from django.contrib import messages

from Vehiculo.models import Turno_de_recorrido
from Vehiculo.forms import Turno_de_recorridoForm


def index(request):
    return render(request, "Vehiculo/index.html")


def turno_de_recorrido_list(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Turno_de_recorrido.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Turno_de_recorrido.objects.all()
    contexto = {"Vehiculo": consulta}
    return render(request, "Vehiculo/turno_de_recorrido_list.html", contexto)


def turno_create(request):  
    if request.method == "POST":  
        form = Turno_de_recorridoForm(request.POST)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Record created successfully.")  
            # return redirect("Vehiculo:turno_de_recorrido_list")  
    else:  # GET  
        form = Turno_de_recorridoForm()  
    return render(request, "Vehiculo/turno_form.html", {"form": form})


def turno_detail(request, pk: int):
    consulta = Turno_de_recorrido.objects.get(id=pk)
    contexto = {"Vehiculo": consulta}
    return render(request, "Vehiculo/turno_detail.html", contexto)


def turno_update(request, pk: int):
    consulta = Turno_de_recorrido.objects.get(id=pk)
    if request.method == "POST":
        form = Turno_de_recorridoForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("Vehiculo:turno_de_recorrido_list")
    else:  # GET
        form = Turno_de_recorridoForm(instance=consulta)
    return render(request, "Vehiculo/turno_form.html", {"form": form})


def turno_delete(request, pk: int):
    consulta = Turno_de_recorrido.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("Vehiculo:turno_de_recorrido_list")
    return render(request, "Vehiculo/turno_confirm_delete.html", {"object": consulta})
