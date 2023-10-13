# Importacion del Modelo
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionCargadorHora import HistorialUtilizacionCargadorHora

# Importacion del paquete serializers
from rest_framework import serializers

# Definicion de HistorialUtilizacionCargadorHoraSerializer
class HistorialUtilizacionCargadorHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialUtilizacionCargadorHora
        fields = '__all__'
        read_only_fields = ('id', 'cargador_id', 'hora_id', 'bus_id')