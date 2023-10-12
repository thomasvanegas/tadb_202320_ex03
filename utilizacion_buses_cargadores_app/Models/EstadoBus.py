# Importamos el paquete models
from django.db import models

# Definicion del modelo (tabla) EstadoBus - Cada modelo es una clase de la subclase models.Model
class EstadoBus(models.Model):
    id = models.AutoField("Identificador de cada estado que puede tener un bus", primary_key=True, editable=False)
    descripcion = models.CharField("Tipo de estado que puede tener un bus", max_length=30, unique=True)
    
    def __str__(self) -> str:
        return super().__str__()