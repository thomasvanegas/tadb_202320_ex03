from django.db import models
# from django.db.models import Model
from utilizacion_buses_cargadores_app.Models import Hora, Cargador, Bus

class HistorialUtilizacionCargadorHora (models.Model):
    id = models.AutoField("Identiicador Unico del Historial", primary_key=True, editable=False)
    cargador = models.ForeignKey(Cargador.Cargador, on_delete=models.CASCADE, to_field='id')
    hora = models.ForeignKey(Hora.Hora, on_delete=models.CASCADE, to_field='id')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, to_field='id', null=True)

    class Meta:
        app_label = 'utilizacion_buses_cargadores_app'
        db_table = 'historial_utilizacion_cargadores_hora'