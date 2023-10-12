# Importamos el paquete models
from django.db import models

# Definicion del modelo (tabla) EstadoCargador - Cada modelo es una clase de la subclase models.Model
class EstadoCargador(models.Model):
    id = models.AutoField("Identificador de cada estado que puede tener Cargador", primary_key=True, editable=False)
    descripcion = models.CharField("Tipos Estados que puede tener un Cargador", max_length=30, unique=True)