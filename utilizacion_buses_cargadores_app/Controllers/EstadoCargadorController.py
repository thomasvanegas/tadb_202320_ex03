
# Importacion de paquetes
from rest_framework import viewsets
from rest_framework import permissions

# Importacion del Modelo y el Serializador
from utilizacion_buses_cargadores_app.Serializers.EstadoCargadorSerializer import EstadoCargadorSerializer
from utilizacion_buses_cargadores_app.Models.EstadoCargador import EstadoCargador

# Definicion del Controlador -> ¿Qué Requests se van a realizar?
class EstadoCargadorController (viewsets.ModelViewSet):
    # El ORM define qué elementos del Modelo serán obtenidos mediante HTTP VERBS
    queryset = EstadoCargador.objects.all() # Consultará todos los datos de la tabla estado_cargador
    serializer_class = EstadoCargadorSerializer
    # ¿A qué atributos tendrá acceso el cliente mediante sus verbos?
    permission_classes = [permissions.AllowAny]