#Procedimiento almacenado para crear registro del bus 
CREATE OR REPLACE FUNCTION crear_bus(id str, placa str, estadoo_id int)
RETURNS void AS $$
BEGIN
    INSERT INTO Bus(id, placa, estadoo_id) VALUES (id, placa, estadoo_id);
END;
$$ LANGUAGE plpgsql;

#Procedimiento almacenado para eliminar  registro del bus 
CREATE OR REPLACE FUNCTION eliminar_bus(id str, placa str, estadoo_id int)
RETURNS void AS $$
BEGIN
    DELETE FROM Bus WHERE id = estado_id;
END;
$$ LANGUAGE plpgsql;

# Llamar procedimiento almacenado desde Django 
from django.db import connection
from django.http import HttpResponse

def crear_bus(id, placa, estado_id):
    with connection.cursor() as cursor:
        cursor.callproc('crear_bus', [id, placa, estado_id])
    return HttpResponse("Bus creado con éxito.")

def eliminar_bus(id):
    with connection.cursor() as cursor:
        cursor.callproc('eliminar_bus', [id])
    return HttpResponse("Bus eliminado con éxito.")
