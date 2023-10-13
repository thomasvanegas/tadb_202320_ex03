# Importar Models
from utilizacion_buses_cargadores_app.Models.UtilizacionCargadorBus import UtilizacionCargadorBus 

class IUtilizacionCargadorBusRepository: 
    def GetAllAsync(self) -> List[UtilizacionCargadorBus]:
        pass
    
    def GetBybus_idAsync(self, bus_id: int) -> UtilizacionCargadorBus:
        pass
    
    def GetBycargador_idAsync(self, cargador_id: int) -> UtilizacionCargadorBus:
        pass
    
    def GetByhora_idAsync(self, hora_id: int) -> UtilizacionCargadorBus:
        pass
    
    def CreateAsync(self, unaUtilizacionCargadorBus:  UtilizacionCargadorBus) -> bool:
        pass

    def UpdateAsync(self, unaUtilizacionCargadorBus:  UtilizacionCargadorBus) -> bool:
        pass

    def DeleteAsync(self, unaUtilizacionCargadorBus:  UtilizacionCargadorBus) -> bool:
        pass
      
      print('Interface de UtilizacionCargadorBus Repository')
