# Importacion del Modelo
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionBusHora import HistorialUtilizacionBusHora

# Importacion del paquete serializers
from rest_framework import serializers

# Definicion de HistorialUtilizacionBusHoraSerializer
class HistorialUtilizacionBusHoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialUtilizacionBusHora
        fields = '__all__'
        read_only_fields = ('id', 'bus_id', 'hora_id')