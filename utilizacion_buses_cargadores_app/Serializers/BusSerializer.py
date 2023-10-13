# SERIALIZAR UN OBJETO PYTHON A UN OBJETO JSON -> SERIALIZAR ES UN DE LOS PRINCIPIOS REST
from utilizacion_buses_cargadores_app.Models.Bus import Bus

# IMPORTAR EL PAQUETE SERIALIZERS
from rest_framework import serializers

# CREANDO EL SERIALIZADOR PARA EL MODELO (TABLA) BUS
class BusSerilizer (serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'
        read_only_fields = ('id', )