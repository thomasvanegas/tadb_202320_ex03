from django.db import models
# from django.db.models import Model
from utilizacion_buses_cargadores_app.Models import Hora, Cargador

class HistorialUtilizacionCargadorHora (models.Model):
    id = models.AutoField("Identiicador Unico del Historial", primary_key=True, editable=False)
    cargador_id = models.ForeignKey(Cargador, on_delete=models.CASCADE, to_field='id')
    hora_id = models.ForeignKey(Hora, on_delete=models.CASCADE, to_field='id')