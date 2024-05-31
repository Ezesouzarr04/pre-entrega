from django.urls import path
from . import views
from Vehiculo.views import turno_list, index

app_name = "Vehiculo"

urlpatterns = [
    path("", views.index, name="index"),
    path("Vehiculo/list", turno_list, name="turno_list"),
]
