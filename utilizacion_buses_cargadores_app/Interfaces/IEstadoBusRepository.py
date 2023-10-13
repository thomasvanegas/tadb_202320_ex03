# Importar Models
from utilizacion_buses_cargadores_app.Models.EstadoBus import EstadoBus   

class IEstadoBusRepository: 
    def GetAllAsync(self) -> List[EstadoBus]:
        pass
    
    def GetByidAsync(self, id: int) -> EstadoBus:
        pass

    def GetBydescripcionAsync(self, descripcion: str) -> EstadoBus:
        pass
    
    def CreateAsync(self, unEstadoBus: EstadoBus) -> bool:
        pass

    def UpdateAsync(self, unEstadoBus: EstadoBus) -> bool:
        pass

    def DeleteAsync(self, unEstadoBus: EstadoBus) -> bool:
        pass

print('Interface del EstadoBus Repository')
