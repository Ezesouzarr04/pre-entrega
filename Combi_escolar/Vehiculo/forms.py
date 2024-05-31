from django import forms

from . import models


class Turno_de_recorridoForm(forms.ModelForm):
    class Meta:
        model = models.Turno_de_recorrido
        fields = ["nombre", "combi", "conductor", "pasajero"]

