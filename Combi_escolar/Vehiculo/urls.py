from django.urls import path
from Vehiculo.views import (
    index,
    turno_de_recorrido_list,
    turno_create,
    turno_detail,
    turno_update,
    turno_delete,
)

app_name = "Vehiculo"

urlpatterns = [
    path("", index, name="index"),
    path("turno_de_recorrido_list/", turno_de_recorrido_list, name="turno_de_recorrido_list"),
    path("turno_create/", turno_create, name="turno_create"),
    path("turno_detail/<int:pk>", turno_detail, name="turno_detail"),
    path("turno_update/<int:pk>", turno_update, name="turno_update"),
    path("turno_delete/<int:pk>", turno_delete, name="turno_delete"),
]
