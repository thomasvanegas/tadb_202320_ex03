# Importamos el paquete models
from django.db import models
from utilizacion_buses_cargadores_app.Models import EstadoCargador

class Cargador (models.Model):
    id = models.AutoField("Identificador Único de Cada Cargador", primary_key=True, editable=False)
    estado_id = models.ForeignKey(EstadoCargador.EstadoCargador, on_delete=models.CASCADE, to_field='id')

    class Meta:
        app_label = 'utilizacion_buses_cargadores_app'
        db_table = 'cargadores'