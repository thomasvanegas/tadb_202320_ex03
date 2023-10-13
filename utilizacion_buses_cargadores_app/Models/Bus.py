# Importamos el paquete models
from django.db import models
from utilizacion_buses_cargadores_app.Models import EstadoBus # Importamos la clase EstadoBus

# Cada modelo (tabla) es una clase de la subclase models.Model
class Bus(models.Model):
    id = models.AutoField("Identificador Único de Cada Bus", primary_key=True, editable=False)
    placa = models.CharField("Placa del Bus", max_length=6, db_index=True)
    estado_id = models.ForeignKey(EstadoBus.EstadoBus, on_delete=models.CASCADE, to_field='id')

    class Meta:
        app_label = 'utilizacion_buses_cargadores_app'
        db_table = 'buses'
