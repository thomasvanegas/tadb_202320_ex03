from utilizacion_buses_cargadores_app.Models import Hora
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class HoraService:
    def create_hora(id, descripcion, hora_pico):
        try:
            if not (5 <= hora_pico <= 9) and not (16 <= hora_pico <= 20):
                raise ValidationError("La hora pico debe estar entre 5 y 9 am o 4 y 8 pm.")
            hora= Hora(id=id, descripcion=descripcion, hora_pico=hora_pico)
            hora.full_clean()  
            hora.save()
            return hora
        except ValidationError as e:
            raise e  
        except ObjectDoesNotExist:
            raise Exception("La hora no existe.")
