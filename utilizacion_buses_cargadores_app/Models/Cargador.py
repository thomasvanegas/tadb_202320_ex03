# Importamos el paquete models
from django.db import models
from utilizacion_buses_cargadores_app.Models import EstadoCargador

class Cargador (models.Model):
    id = models.AutoField("Identificador Único de Cada Cargador", primary_key=True, editable=False)
    estado_id = models.ForeignKey(EstadoCargador, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return super().__str__()