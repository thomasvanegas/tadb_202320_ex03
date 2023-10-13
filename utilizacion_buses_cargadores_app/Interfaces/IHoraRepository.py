# Importar Models
from utilizacion_buses_cargadores_app.Models.Hora import Hora  

class IHoraRepository: 
    def GetAllAsync(self) -> List[Hora]:
        pass
    
    def GetByidAsync(self, id: int) -> Hora:
        pass

    def GetBydescripcionAsync(self, descripcion: str) ->  Hora:
        pass
    
    def GetByhora_picoAsync(self, hora_pico: bool) ->  Hora:
        pass
    
    def CreateAsync(self, unaHora:  Hora) -> bool:
        pass

    def UpdateAsync(self, unaHora:  Hora) -> bool:
        pass

    def DeleteAsync(self, unaHora:  Hora) -> bool:
        pass

print('Interface de la Hora Repository')
