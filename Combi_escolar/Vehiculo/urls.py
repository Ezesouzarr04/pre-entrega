from django.urls import path

from . import views

app_name = "Vehiculo"

urlpatterns = [
    path("", views.index, name="index"),
]
