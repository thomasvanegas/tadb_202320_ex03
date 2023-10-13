# Importar Models
from utilizacion_buses_cargadores_app.Models.Bus import Bus  

class IBusRepository: 
    def GetAllAsync(self) -> List[Bus]:
        pass
    
    def GetByidAsync(self, id: int) -> Bus:
        pass

    def GetByplacaAsync(self, placa: str) -> Bus:
        pass
        
    def GetByestado_idAsync(self, estado_id: int) -> Bus:
        pass
    
    def CreateAsync(self, unBus: Bus) -> bool:
        pass

    def UpdateAsync(self, unBus: Bus) -> bool:
        pass

    def DeleteAsync(self, unBus: Bus) -> bool:
        pass
print('Interface del Bus Repository')
