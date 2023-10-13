# Importacion del Modelo
from utilizacion_buses_cargadores_app.Models.Cargador import Cargador

# Importacion del paquete serializers
from rest_framework import serializers

# Definicion de CargadorSerializer
class CargadorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cargador
        fields = '__all__'
        read_only_fields = ('id', )