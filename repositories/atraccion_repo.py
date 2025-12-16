from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.atraccion_model import AtraccionModel
import json

class AtraccionRepo:
    @staticmethod
    def crear_atraccion(nombre, tipo, altura_minima, activa, fecha_inauguracion, detalles_json = None):
        try:
            if detalles_json:
                return AtraccionModel.create(nombre=nombre, tipo=tipo, altura_minima=altura_minima, detalles=detalles_json, activa=activa, fecha_inauguracion=fecha_inauguracion)
            else:
                return AtraccionModel.create(nombre=nombre, tipo=tipo, altura_minima=altura_minima, activa=activa, fecha_inauguracion=fecha_inauguracion)
        except Exception as e:
            print(f"Error insertando la atraccion: {e}")
            return None

    @staticmethod
    def mostrar_todas():
        try:
            return list(AtraccionModel.select())
        except Exception as e:
            print(f"Error al obtener las atracciones")
            return None
    
    @staticmethod
    def mostrar_activas():
        try:
            return list(AtraccionModel.select().where(AtraccionModel.activa == True))
        except Exception as e:
            print(f"Error al obtener atracciones 'activas'")
            return None
    
    # PENDIENTE COMO HACER CON NUMEROS #
    @staticmethod
    def mostrar_intensidad():
        pass

    @staticmethod
    def mostrar_duracion():
        pass
    ##########################################
    
    @staticmethod
    def mostrar_looping_caida():
        try:
            return list(AtraccionModel.select().where(AtraccionModel.detalles["caracteristicas"].contains(["looping"]) & AtraccionModel.detalles["caracteristicas"].contains(["caida_libre"])))
        except Exception as e:
            print(f"Error al obtener atracciones con 'caida libre' y 'looping':{e}")
            return None

    @staticmethod
    def mostrar_mantenimiento_programado():
        try:
            return list(AtraccionModel.select().where(AtraccionModel.detalles["horarios"]["mantenimiento"].is_null(False)))
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
    def anyadir_caracteristica_atraccion(atraccion_id, caracteristica):
        try:
            atraccion = AtraccionRepo.buscar_id(atraccion_id)
            if atraccion: # en caso de existir la atraccion introducida
                caracteristicas = atraccion.detalles["caracteristicas"]
                if caracteristica not in caracteristicas: # en caso de no estar la caracteristica en la lista de caracteristicas de la atraccion
                    caracteristicas.append(caracteristica) # anyadirmos la caracteristica a la lista almacenada en el jsonb
                    atraccion.detalles["caracteristicas"] = caracteristicas # asignacion de la lista modificada 
                    atraccion.save()
                else:
                    print("La caracteristica indicada ya se encuentra entre las caracteristicas de la atraccion introducida")
            else:
                print("La atraccion introducida no existe")
        except Exception as e:
            print(f"Error al anyadir la caracteristica a la atraccion: {e}")
            return None

    @staticmethod
    def cambiar_estado(id):
        try:
            atraccion = AtraccionRepo.buscar_id(id)
            if not atraccion:
                print(f"Atraccion con id {id} no encontrada.")
                return
            if atraccion.activa:
                atraccion.activa = False
            else:
                atraccion.activa = True
            atraccion.save()
            print(f"El estado de la atraccion {id} se ha cambiado a {atraccion.activa}")
            return atraccion
        except Exception as e:
            print(f"Error al cambiar el esdado de la atraccion con id {id}: {e}")
            return None

    @staticmethod
    def eliminar_id(id):
        try:
            query = AtraccionModel.delete().where(AtraccionModel.id==id)
            eliminado = query.execute()
            if eliminado == 0:
                print(f"No se encontro la atraccion con id: {id}")
            return eliminado
        except Exception as e:
            print(f"Error al eliminar la atraccion {e}")