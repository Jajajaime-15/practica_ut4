from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.visitante_model import VisitanteModel
import json

class VisitanteRepo:
    @staticmethod
    def crear_visitante(nombre, email, altura,preferencias_json=None):
        try:
            if preferencias_json:
                return VisitanteModel.create(nombre=nombre, email=email, altura=altura, preferencias=preferencias_json)
            else:
                return VisitanteModel.create(nombre=nombre, email=email, altura=altura)
        except Exception as e:
            print(f"Error insertando al visitante: {e}")
            return None
    
    @staticmethod
    def mostrar_todos():
        try:
            return list(VisitanteModel.select())
        except Exception as e:
            print(f"Error al obtener los visitantes: {e}")
            
    @staticmethod
    def buscar_id(id):
        try:
            return VisitanteModel.get(VisitanteModel.id == id)
        except Exception as e:
            print(f"Error buscando el visitante con id {id}: {e}")
            return None
    
    @staticmethod
    def mostrar_extremas():
        try:
            return list(VisitanteModel.select().where(VisitanteModel.preferencias["tipo_favorito"] == "extrema"))
        except Exception as e:
            print(f"Error al obtener visitantes con preferecncia por atracciones extremas: {e}")
            return None

    @staticmethod
    def mostrar_cardio():
        try:
            return list(VisitanteModel.select().where(VisitanteModel.preferencias["restricciones"].contains(["problemas_cardiacos"])))
        except Exception as e:
            print(f"Error al obtener visitantes con problemas cardiacos: {e}")
            return None

    @staticmethod
    def eliminar_visitante(id):
        try:
            query = VisitanteModel.delete().where(VisitanteModel.id==id)
            eliminado = query.execute()
            if eliminado == 0:
                print(f"No hay ningun visitante con el id {id}")
            return eliminado
        except Exception as e:
            print(f"Error al eliminar al visitante con id {id}: {e}")

    @staticmethod
    def eliminar_restriccion_visitante(visitante_id, restriccion):
        try:
            visitante = VisitanteRepo.buscar_id(visitante_id)
            if visitante: # en caso de existir el visitante introducido
                restricciones = visitante.preferencias["restricciones"]
                if restriccion in restricciones: # en caso de estar la restriccion en la lista de restricciones del visitante
                    restricciones.remove(restriccion) # eliminacion de la restriccion almacenada en el jsonb
                    visitante.preferencias["restricciones"] = restricciones # asignacion de la lista modificada 
                    visitante.save()
                else:
                    print("La restriccion indicada no se encuentra entre las restricciones del visitante introducido")
            else:
                print("El visitante introducido no existe")
        except Exception as e:
            print(f"Error al eliminar la restriccion del visitante: {e}")
            return None
        

    
