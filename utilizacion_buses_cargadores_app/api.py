
# from directorio.subdirectorio import Clase
from django.contrib import admin

#¿Quién puede consultar?, ¿Qué peticiones puede recibir?
from rest_framework import viewsets 
from rest_framework import permissions

# Importacion del Modelo y el Serializer
from utilizacion_buses_cargadores_app.Models.EstadoBus import EstadoBus
from utilizacion_buses_cargadores_app.serializers import EstadoBusSerializer

# Se define el viewset para el modelo EstadoBus
class EstadoBusViewSet (viewsets.ModelViewSet):
    """
    Definimos qué consultas mediante verbos HTTP se van a poder realizar
    """
    queryset = EstadoBus.objects.all() # consulta todos los datos de una tabla
    permission_classes = [permissions.AllowAny] # Cualquier cliente puede solicitar datos isAutheticate
    serializer_class = EstadoBusSerializer