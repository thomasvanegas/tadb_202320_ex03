# Importar Models
from utilizacion_buses_cargadores_app.Models.HistorialUtilizacionCargadorHora import HistorialUtilizacionCargadorHora  

class IHistorialUtilizacionCargadorHoraRepository: 
    def GetAllAsync(self) -> List[HistorialUtilizacionCargadorHora]:
        pass
    
    def GetByidAsync(self, id: int) -> HistorialUtilizacionCargadorHora:
        pass

    def GetBycargador_idAsync(self, cargador_id: int) ->  HistorialUtilizacionCargadorHora:
        pass
    
    def GetByhora_idAsync(self, hora_id: int) ->  HistorialUtilizacionCargadorHora:
        pass
    
    def CreateAsync(self, unHistorialUtilizacionCargadorHora:  HistorialUtilizacionCargadorHora) -> bool:
        pass

    def UpdateAsync(self, unHistorialUtilizacionCargadorHora:  HistorialUtilizacionCargadorHora) -> bool:
        pass

    def DeleteAsync(self, unHistorialUtilizacionCargadorHora:  HistorialUtilizacionCargadorHora) -> bool:
        pass
      
print('Interface del HistorialUtilizacionCargadorHora Repository')
