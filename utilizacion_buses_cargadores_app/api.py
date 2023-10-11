# from directorio.subdirectorio import Clase
from utilizacion_buses_cargadores_app.models import EstadoBus
from rest_framework import viewsets #¿Quién puede consultar?, ¿Qué peticiones puede recibir?
from rest_framework import permissions
from utilizacion_buses_cargadores_app.serializers import EstadoBusSerializer

# Se define el viewset para el modelo EstadoBus
class EstadoBusViewSet (viewsets.ModelViewSet):
    """
    Definimos qué consultas mediante verbos HTTP se van a poder realizar
    """
    queryset = EstadoBus.objects.all() # consulta todos los datos de una tabla
    permission_classes = [permissions.AllowAny] # Cualquier cliente puede solicitar datos isAutheticate
    serializer_class = EstadoBusSerializer