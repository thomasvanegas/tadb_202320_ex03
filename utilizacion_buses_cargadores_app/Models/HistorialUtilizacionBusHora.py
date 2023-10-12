from django.db import models
# from django.db.models import Model
from utilizacion_buses_cargadores_app.Models import Bus, Hora

class HistorialUtilizacionBusHora (models.Model):
    id = models.AutoField("Identiicador Unico del Historial", primary_key=True, editable=False)
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE, to_field='id')
    hora_id = models.ForeignKey(Hora.Hora, on_delete=models.CASCADE, to_field='id')