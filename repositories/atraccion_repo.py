from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.atraccion_model import AtraccionModel
from models.ticket_model import TicketModel
from models.visitante_model import VisitanteModel
import json

class AtraccionRepo:
    @staticmethod
    def crear_atraccion(nombre, tipo, altura_minima, detalles_json = None):
        try:
            # creamos una atraccion nueva, teniendo en cuenta si tiene informacion en detalles o no
            if detalles_json:
                return AtraccionModel.create(nombre=nombre, tipo=tipo, altura_minima=altura_minima, detalles=detalles_json)
            else:
                return AtraccionModel.create(nombre=nombre, tipo=tipo, altura_minima=altura_minima)
        except Exception as e:
            print(f"Error insertando la atraccion: {e}")
            return None

    @staticmethod
    def mostrar_todas():
        try:
            # select para mostrar todas las atracciones
            return list(AtraccionModel.select())
        except Exception as e:
            print(f"Error al obtener las atracciones")
            return None
    
    @staticmethod
    def mostrar_activas():
        try:
            # mostramos solo las atracciones con el campo 'activa' sea True
            return list(AtraccionModel.select().where(AtraccionModel.activa == True))
        except Exception as e:
            print(f"Error al obtener atracciones 'activas'")
            return None
        
    @staticmethod
    def mostrar_intensidad():
        try:
            # convertimos la intensidad del JSON a integer usando CAST en SQL y poder comparar el valor que sea mayor que 7
            return list(AtraccionModel.select().where(SQL("CAST(detalles->>'intensidad' AS INTEGER) > 7")))
        except Exception as e:
            print(f"Error al mostrar las atracciones con intensidad mayor que 7: {e}")
            return None

    @staticmethod
    def mostrar_duracion():
        try:
            # convertimos la duracion_segundos del JSON a integer usando CAST en SQL y poder comparar el valor que sea mayor que 120
            return list(AtraccionModel.select().where(SQL("CAST(detalles->>'duracion_segundos' AS INTEGER) > 120")))
        except Exception as e:
            print(f"Error al mostrar las atracciones con duracion mayor que 120 segundos: {e}")
            return None
    
    @staticmethod
    def mostrar_looping_caida():
        try:
            # para obtener las atracciones que tienen incluidas en sus caracteristicas looping y caida libre, usamos contains sobre el JSON
            return list(AtraccionModel.select().where(AtraccionModel.detalles["caracteristicas"].contains(["looping"]) & AtraccionModel.detalles["caracteristicas"].contains(["caida_libre"])))
        except Exception as e:
            print(f"Error al obtener atracciones con 'caida libre' y 'looping':{e}")
            return None

    @staticmethod
    def mostrar_mantenimiento_programado():
        try:
            # para poder obtener la longitud de la lista de mantenimiento debemos usar la funcion propia de jsonb dentro del propio SQL
            return list(AtraccionModel.select().where(SQL("jsonb_array_length(detalles->'horarios'->'mantenimiento') > 0"))) # si se comparase fuera no detectaria la lista como vacia
        except Exception as e:
            print(f"Error al obtener atracciones con un mantenimiento programado: {e}")
            return None

    @staticmethod
    def buscar_id(id):
        try:
            return AtraccionModel.get(AtraccionModel.id == id)
        except Exception as e:
            print(f"Error buscando la atraccion con id {id}: {e}")
            return None
        
    @staticmethod
    def cambiar_estado(id):
        try:
            # utilizamos el metodo de buscar por id una atraccion
            atraccion = AtraccionRepo.buscar_id(id)
            if not atraccion:
                print(f"Atraccion con id {id} no encontrada.")
                return
            # cambiamos el estado de la atraccion, si esta a True la pasamos a False o al reves
            if atraccion.activa:
                atraccion.activa = False
            else:
                atraccion.activa = True
            # guardamos el cambio
            atraccion.save()
            print(f"El estado de la atraccion {id} se ha cambiado a {atraccion.activa}")
            return atraccion
        except Exception as e:
            print(f"Error al cambiar el esdado de la atraccion con id {id}: {e}")
            return None

    @staticmethod
    def eliminar_atraccion(id):
        try:
            # pedimos confirmacion al usuario antes de eliminar definitivamente la atraccion
            confirmar = input("Estas seguro de querer eliminar la atraccion? [s/n]").strip()
            if confirmar == "s" or confirmar == "si":
                # hacemos un delete buscando por el id
                query = AtraccionModel.delete().where(AtraccionModel.id==id)
                eliminado = query.execute()
                if eliminado == 0:
                    print(f"No se encontro la atraccion con id: {id}")
                else:
                    print("Atraccion eliminada correctamente")
            else:
                print("Se ha cancelado la operacion de eliminacion")
        except Exception as e:
            print(f"Error al eliminar la atraccion {e}")

    # obtener las 5 atracciones más vendidas (en tickets específicos)  
    @staticmethod
    def atracciones_mas_vendidas():
    # contamos cuántos tickets tiene cada atracción
        return list(
            TicketModel.select(TicketModel.atraccion_id, fn.COUNT(TicketModel.id).alias('total_tickets'))
            .where(TicketModel.atraccion_id.is_null(False))  # solo tickets con atraccion, que no sean generales
            .group_by(TicketModel.atraccion_id)  # agrupar por atracción
            .order_by(fn.COUNT(TicketModel.id).desc())  # ordenar de mayor a menor
            .limit(5)  # tomar solo los 5 primeros
        )
    
    # atracciones compatibles para un visitante (Atracciones activas que coincidan en tipo, y donde el usuario cumpla con el mínimo de altura)
    @staticmethod
    def atracciones_compatibles(visitante_id):
        try:
             return list(
            AtraccionModel.select(
            AtraccionModel.nombre,
            AtraccionModel.tipo,
            AtraccionModel.altura_minima
        )
        .join(TicketModel, on=(AtraccionModel.id == TicketModel.atraccion_id))
        .join(VisitanteModel, on=(TicketModel.visitante_id == VisitanteModel.id))
        .where(AtraccionModel.activa == True,
            VisitanteModel.id == visitante_id,
            AtraccionModel.altura_minima <= VisitanteModel.altura,
            AtraccionModel.tipo == VisitanteModel.preferencias["tipo_favorito"])  # ← CORREGIDO
        .order_by(AtraccionModel.tipo, AtraccionModel.nombre)
    )
        except Exception as e:
            print(f"Error al buscar las atracciones compatibles con el visitante: {e}")
    
    # Modificaciones en jsonb
    @staticmethod
    def anyadir_caracteristica_atraccion(atraccion_id, caracteristica):
        try:
            atraccion = AtraccionRepo.buscar_id(atraccion_id)
            if atraccion: # en caso de existir la atraccion introducida
                caracteristicas = atraccion.detalles["caracteristicas"]
                if caracteristica not in caracteristicas: # en caso de no estar la caracteristica en la lista de caracteristicas de la atraccion
                    caracteristicas.append(caracteristica) # anyadiremos la caracteristica a la lista almacenada en el jsonb
                    atraccion.detalles["caracteristicas"] = caracteristicas # asignacion de la lista modificada 
                    atraccion.save()
                else:
                    print("La caracteristica indicada ya se encuentra entre las caracteristicas de la atraccion introducida")
            else:
                print("La atraccion introducida no existe")
        except Exception as e:
            print(f"Error al anyadir la caracteristica a la atraccion: {e}")
            return None
