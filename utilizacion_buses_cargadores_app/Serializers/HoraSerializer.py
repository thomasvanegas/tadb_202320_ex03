# Importacion del Modelo
from utilizacion_buses_cargadores_app.Models.Hora import Hora

# IMPORTAR EL PAQUETE SERIALIZERS
from rest_framework import serializers

# CREANDO EL SERIALIZADOR PARA EL MODELO (TABLA) Hora
class HoraSerilizer (serializers.ModelSerializer):
    class Meta:
        model = Hora
        fields = '__all__'
        read_only_fields = ('id', 'descripcion', 'hora_pico', )