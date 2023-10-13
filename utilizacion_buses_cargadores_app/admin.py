from django.contrib import admin
from utilizacion_buses_cargadores_app.Models.Bus import Bus
from utilizacion_buses_cargadores_app.Models.EstadoBus import EstadoBus
from utilizacion_buses_cargadores_app.Models.Cargador import Cargador
from utilizacion_buses_cargadores_app.Models.EstadoCargador import EstadoCargador
from utilizacion_buses_cargadores_app.Models.Hora import Hora
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionBusHora import HistorialUtilizacionBusHora
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionCargadorHora import HistorialUtilizacionCargadorHora

# Register your models here -> Para que sean visible a través del panel de administracion
admin.site.register(Bus)
admin.site.register(EstadoBus)
admin.site.register(Cargador)
admin.site.register(EstadoCargador)
admin.site.register(Hora)
admin.site.register(HistorialUtilizacionBusHora)
admin.site.register(HistorialUtilizacionCargadorHora)
