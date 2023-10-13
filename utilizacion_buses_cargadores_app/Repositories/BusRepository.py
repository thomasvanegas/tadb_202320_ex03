# Repository <=> Viewset

# Importacion de Paquetes viewsets y permissions
from rest_framework import viewsets, permissions

# Importacion del Modelo Bus y el serilizer BusSerializer
from utilizacion_buses_cargadores_app.Models.Bus import Bus
from utilizacion_buses_cargadores_app.Serializers.BusSerializer import BusSerilizer

class BusRepository (viewsets.ModelViewSet):
    # El ORM define qué elementos del Modelo serán obtenidos mediante HTTP VERBS
    queryset = Bus.objects.all() # Consultará todos los datos de la tabla estado_cargador
    serializer_class = BusSerilizer
    # ¿A qué atributos tendrá acceso el cliente mediante sus verbos?
    permission_classes = [permissions.AllowAny]