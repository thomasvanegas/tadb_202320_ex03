# Invocando el módulo de django rest framework
from rest_framework import serializers
from .models import EstadoBus #Importar un modelo ya definido

class EstadoBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoBus # Nombre del modelo
        fields = ('id', 'descripcion') # Campos que pueden ser consultados de ese modelo (TUPLA)
        read_only_fields = ('id', ) # Indicamos que el id no se puede modificar, No Update, No delete -> coma porque django detecta string