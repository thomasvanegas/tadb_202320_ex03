# from directorio.subdirectorio import Clase
from django.contrib import admin
from utilizacion_buses_cargadores_app.Models.Bus import Bus
from utilizacion_buses_cargadores_app.Models.EstadoBus import EstadoBus
from utilizacion_buses_cargadores_app.Models.Cargador import Cargador
from utilizacion_buses_cargadores_app.Models.EstadoCargador import EstadoCargador
from utilizacion_buses_cargadores_app.Models.Hora import Hora
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionBusHora import HistorialUtilizacionBusHora
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionCargadorHora import HistorialUtilizacionCargadorHora
from utilizacion_buses_cargadores_app.Models.UtilizacionCargadorBus import UtilizacionCargadorBus
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