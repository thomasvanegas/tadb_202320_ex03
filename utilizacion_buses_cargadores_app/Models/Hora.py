from django.db import models

class Hora (models.Model):
    id = models.AutoField("Identificador de Cada Hora", primary_key=True, editable=False)
    descripcion = models.CharField("Descripcion de Hora", max_length=4)
    hora_pico = models.BooleanField("Define si la Hora es Pico o No")

    class Meta:
        app_label = 'utilizacion_buses_cargadores_app'
        db_table = 'horas'