
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls


# Definicion de rutas - basadas en _app/urls/
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('utilizacion_buses_cargadores_app.Controllers')),
    #path('api/estados_cargadores/', include('utilizacion_buses_cargadores_app.Controllers.EstadoCargadorController')),
    path('docs/', include_docs_urls(title='Documentacion API')),
    path('api/buses/', include('utilizacion_buses_cargadores_app.Controllers.BusController'))
]
