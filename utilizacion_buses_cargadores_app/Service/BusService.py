from utilizacion_buses_cargadores_app.Helpers import AppValidationException, DbOperationException
from utilizacion_buses_cargadores_app.Interfaces import BusRepository
from utilizacion_buses_cargadores_app.Models import Bus

class BusService:
    def __init__(self, bus_repository:  BusRepository):
        self._bus_repository= bus_repository

    async def get_all_async(self):
        return await self._bus_repository.get_all_async()
    
    async def get_details_by_id_async(self, bus_id):
        unbus = await self._bus_repository.get_details_by_id_async(bus_id)
        if unbus.id == 0:
            raise AppValidationException(f"No se encontro el bus con el id {bus_id}")
        return unbus
 
    async def create_async(self, bus):
        if not bus.placa:
            raise AppValidationException("No se puede insertar una placa nula")
        if not bus.estado_id:
            raise AppValidationException("No se puede insertar un estado nulo")
        
        bus_existente = await self._bus_repository.get_by_placa_async(bus.placa)
        
        if bus_existente.id != 0:
            raise AppValidationException(f"Existe un bus con la placa {bus.placa}")
        try:
             bus_resultado= await self._bus_repository.create_async(bus)
        
            if not bus_resultado:
                raise AppValidationException("No se agregaron cambios")
            bus_existente = await self._bus_repository.get_by_placa_async(bus.placa)
        except DbOperationException as error:
            raise error
        return bus_existente
    
    async def delete_async(self, bus_id):
        
        bus_existente = await self._bus_repository.get_by_id_async(bus_id)

        if bus_existente.id == 0:
            raise AppValidationException(f"No existe un bus con el id{bus_id} que se pueda eliminar")

        try:
           bus_resultado = await self._bus_repository.delete_async(bus_existente)

            if not bus_resultado:
                raise AppValidationException(" No generó cambios en la DB")
        except DbOperationException as error:
            raise error
    
