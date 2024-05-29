from django.contrib import admin

from . import models

admin.site.register(models.Combi)
admin.site.register(models.Conductor)
admin.site.register(models.Pasajero)
admin.site.register(models.Turno_de_recorrido)
