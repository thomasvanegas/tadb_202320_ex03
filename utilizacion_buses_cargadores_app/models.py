from django.db import models

# Cada modelo representa una tabla en la BD
# Cada atributo del modelo (Clase) representa un campo o atributo de la tabla

# Tabla estados_buses
class EstadoBus (models.Model):
    id = models.AutoField("Identificador de cada estado que puede tener un bus", primary_key=True)
    descripcion = models.CharField("Tipo de estado que puede tener un bus", max_length=30, unique=True)
