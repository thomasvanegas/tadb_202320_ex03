# Importar Models
from utilizacion_buses_cargadores_app.Models.EstadoCargador import EstadoCargador   

class IEstadoCargadorRepository: 
    def GetAllAsync(self) -> List[EstadoCargador]:
        pass
    
    def GetByidAsync(self, id: int) -> EstadoCargador:
        pass

    def GetBydescripcionAsync(self, descripcion: str) -> EstadoCargador:
        pass
    
    def CreateAsync(self, unEstadoCargador: EstadoCargador) -> bool:
        pass

    def UpdateAsync(self, unEstadoCargador: EstadoCargador) -> bool:
        pass

    def DeleteAsync(self, unEstadoBus: EstadoCargador) -> bool:
        pass

print('Interface del EstadoCargador Repository')
