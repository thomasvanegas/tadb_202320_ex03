from utilizacion_buses_cargadores_app.Models.Bus import Bus
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class BusService:
    
    def create_bus(id, placa, estado_id):
        try:
            if Bus.objects.filter(id=id).exists():
                raise ValidationError("Ya existe un Bus con este id.")
            bus = Bus(id=id, placa=placa, estado_id=estado_id)
            bus.full_clean()
            bus.save()
            return bus
        except ValidationError as e:
            raise e  
            
    def get_bus_by_id(bus_id):
        try:
            return Bus.objects.get(id=bus_id)
        except ObjectDoesNotExist:
            raise Exception("El bus no existe.")
            
    def update_bus(bus_id, id, placa, estado_id):
        try:
            bus = BusService.get_bus_by_id(bus_id)
            
            if Bus.objects.filter(id=id).exclude(id=bus_id).exists():
                raise ValidationError("Ya existe un Bus con este id.")

            bus.id = id
            bus.placa = placa
            bus.estado_id = estado_id
            bus.full_clean() 
            bus.save()
            return bus
            
        except ValidationError as e:
            raise e  # Maneja la validación de reglas de negocio
        except ObjectDoesNotExist:
            raise Exception("El bus no existe.")
    
