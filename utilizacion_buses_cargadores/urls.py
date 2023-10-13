
from django.contrib import admin
from django.urls import path, include


# Definicion de rutas - basadas en _app/urls/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('utilizacion_buses_cargadores_app.urls')),
    path('', include('utilizacion_buses_cargadores_app.Urls.EstadoCargadorUrl'))
]
