
# Importacion de paquetes
from django.urls import path, include
from rest_framework import routers
from utilizacion_buses_cargadores_app.Controllers.EstadoCargadorController import EstadoCargadorController

# Un enrutador permite manejar multiples rutas
router = routers.DefaultRouter()

# Se definen las rutas o endpoints que puede tener la API
router.register(r'api/estados_cargador', EstadoCargadorController, 'estados_cargador')

urlpatterns = router.urls