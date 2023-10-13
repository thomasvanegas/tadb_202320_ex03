# Importar Models
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionBusHora import HistorialUtilizacionBusHora  

class IHistorialUtilizacionBusHoraRepository: 
    def GetAllAsync(self) -> List[HistorialUtilizacionBusHora]:
        pass
    
    def GetByidAsync(self, id: int) -> HistorialUtilizacionBusHora:
        pass

    def GetBybus_idAsync(self, bus_id: int) -> HistorialUtilizacionBusHora:
        pass
    
    def GetByhora_idAsync(self, hora_id: int) -> HistorialUtilizacionBusHora:
        pass
    
    def CreateAsync(self, unHistorialUtilizacionBusHora: HistorialUtilizacionBusHora) -> bool:
        pass

    def UpdateAsync(self, unHistorialUtilizacionBusHora: HistorialUtilizacionBusHora) -> bool:
        pass

    def DeleteAsync(self, unHistorialUtilizacionBusHora: HistorialUtilizacionBusHora) -> bool:
        pass
      print('Interface de HistorialUtilizacionBusHora Repository')
