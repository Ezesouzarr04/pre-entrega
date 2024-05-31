# Nombre del Proyecto

Comisión: 54140

Alumno: Ezequiel Souza Arraigada

## Explicación breve del proyecto en cuanto al servicio

## Explicación breve técnica: urls, modelos, plantillas

## Mejoras futuras

## Problemas conocidos


<!DOCTYPE html>
<html>
<head>
    <title>Lista de Turnos</title>
</head>
<body>
    {% for turno in turnos %}
        <ul>
            <li><h3>{{ turno.nombre }}</h3></li>
            <p>Nombre: {{ turno.nombre }}</p>
            <p>Combi: {{ turno.combi }}</p>
            <p>Conductor: {{ turno.conductor }}</p>
            <p>Pasajero: 
                {% for p in turno.pasajero.all %}
                    {{ p.nombre }}{% if not forloop.last %}, {% endif %}
                {% endfor %}
            </p>
        </ul>
    {% endfor %}
</body>
</html>


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