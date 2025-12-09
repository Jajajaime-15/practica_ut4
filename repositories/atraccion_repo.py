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
        return list(AtraccionModel.select())
    
    @staticmethod
    def mostrar_activas():
        return list(AtraccionModel.select().where(AtraccionModel.activa == True))
    
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
