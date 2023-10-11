from rest_framework import routers
from utilizacion_buses_cargadores_app.api import EstadoBusViewSet

router = routers.DefaultRouter() # permite no definir urlpatterns

router.register('api/estados_buses', EstadoBusViewSet, 'estados_buses') # Crea un get, post, delete, put


# Importando las urls
urlpatterns = router.urls