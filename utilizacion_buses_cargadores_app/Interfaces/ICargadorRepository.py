# Importar Models
from utilizacion_buses_cargadores_app.Models.Cargador import Cargador

class ICargadorRepository: 
    def GetAllAsync(self) -> List[Cargador]:
        pass

    def GetByidAsync(self, id: int) -> Cargador:
        pass

    def GetByestado_idAsync(self, estado_id: int) -> Cargador:
        pass
    def CreateAsync(self, unCargador: Cargador) -> bool:
        pass

    def UpdateAsync(self, unCargador: Cargador) -> bool:
        pass

    def DeleteAsync(self, unCargador: Cargador) -> bool:
        pass

print('Interface del Cargador Repository')
