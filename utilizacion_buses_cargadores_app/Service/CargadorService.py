from utilizacion_buses_cargadores_app.Models import Cargador
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class CargadorService:
    def create_cargador(id, estado_id, ocupado=False):
        try:
          if Cargador.objects.filter(id=id).exists():
            raise ValidationError("Ya existe un Cargador con este id.")
            
            cargador = Cargador(id=id, estado_id=estado_id, ocupado=ocupado)
            cargador = full_clean()  
            cargador.save()
            return cargador
        except ValidationError as e:
            raise e  
        except Exception as e:
            raise e 
          
    def get_cargador_by_id(cargador_id):
        try:
            return Cargador.objects.get(id=cargador_id)
        except ObjectDoesNotExist:
            raise Exception("El cargador no existe.")

    def update_cargador(cargador_id, id, estado_id, ocupado=False):
        try:
          cargador = CargadorService.get_cargador_by_id(cargador_id)
          
          if Cargador.objects.filter(id=id).exclude(id=cargador_id).exists():
                raise ValidationError("Ya existe un Cargador con este id.")
            
            cargador.id = id
            cargador.estado_id = estado_id
            cargador.ocupado = ocupado
            cargador.full_clean()  
            cargador.save()
            return cargador
        except ValidationError as e:
            raise e  
        except ObjectDoesNotExist:
            raise Exception("El cargador no existe.")

        
