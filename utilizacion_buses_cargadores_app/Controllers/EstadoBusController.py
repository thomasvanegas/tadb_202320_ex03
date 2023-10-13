from rest_framework import routers
from utilizacion_buses_cargadores_app.Repositories.EstadoBusRepository import EstadoBusRepository

router = routers.DefaultRouter() # permite no definir urlpatterns

router.register(r'api/estados_bus', EstadoBusRepository, 'estados_bus') # Crea un get, post, delete, put


# Importando las urls
urlpatterns = router.urls