# Invocando el módulo de django rest framework
from rest_framework import serializers
#Importar un modelo ya definido
from django.contrib import admin
from utilizacion_buses_cargadores_app.Models.Bus import Bus
from utilizacion_buses_cargadores_app.Models.EstadoBus import EstadoBus
from utilizacion_buses_cargadores_app.Models.Cargador import Cargador
from utilizacion_buses_cargadores_app.Models.Hora import Hora
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionBusHora import HistorialUtilizacionBusHora
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionCargadorHora import HistorialUtilizacionCargadorHora
from utilizacion_buses_cargadores_app.Models.UtilizacionCargadorBus import UtilizacionCargadorBus

class EstadoBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoBus # Nombre del modelo
        fields = ('id', 'descripcion') # Campos que pueden ser consultados de ese modelo (TUPLA)
        read_only_fields = ('id', ) # Indicamos que el id no se puede modificar, No Update, No delete -> coma porque django detecta string