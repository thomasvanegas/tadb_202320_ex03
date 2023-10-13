# Invocando el paquete Serializers de rest_framework
# Serializar es convertir de python a JSON (Principios de REST)
from rest_framework import serializers 

# Importando el modelo EstadoCargador
from utilizacion_buses_cargadores_app.Models.EstadoCargador import EstadoCargador

# Creando el serializador
class EstadoCargadorSerializer (serializers.ModelSerializer):
    class Meta:
        model = EstadoCargador
        fields = ('id', 'descripcion') # -> '__all__'
        read_only_fields = ('id', )