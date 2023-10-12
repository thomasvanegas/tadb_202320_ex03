# Importacion de paquetes
from django.db import models
from utilizacion_buses_cargadores_app.Models import Bus, Cargador, Hora

class UtilizacionCargadorBus(models.Model):
    id = models.AutoField("Identificador del Historial", primary_key=True, editable=False)
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE, to_field='id')
    cargador_id = models.ForeignKey(Cargador, on_delete=models.CASCADE, to_field='id')
    hora_id = models.ForeignKey(Hora, on_delete=models.CASCADE, to_field='id')