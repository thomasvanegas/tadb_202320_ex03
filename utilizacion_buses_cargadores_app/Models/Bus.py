# Importamos el paquete models
from django.db import models
from utilizacion_buses_cargadores_app.Models import EstadoBus # Importamos la clase EstadoBus
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re

def validar_placa(value):
    if not re.match(r'^[A-Z]{3}\d{3}$', value):
        raise ValidationError('La placa debe tener 3 letras seguidas de 3 números.')

# Cada modelo (tabla) es una clase de la subclase models.Model
class Bus(models.Model):
    id = models.AutoField("Identificador Único de Cada Bus", primary_key=True, editable=False)
    placa = models.CharField("Placa del Bus", validators=[validar_placa], max_length=6, db_index=True)
    estado_id = models.ForeignKey(EstadoBus.EstadoBus, on_delete=models.CASCADE, to_field='id')

    class Meta:
        app_label = 'utilizacion_buses_cargadores_app'
