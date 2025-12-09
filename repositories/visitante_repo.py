from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
import json

class VisitanteRepo:
    @staticmethod
    def crear_visitante(nombre, email, altura, fecha_registro, preferencias_json=None):
        try:
            if preferencias_json:
                return VisitanteModel.create(nombre=nombre, email=email, altura=altura, fecha_registro=fecha_registro, preferencias=preferencias_json)
            else:
                return VisitanteModel.create(nombre=nombre, email=email, altura=altura, fecha_registro=fecha_registro)
        except Exception as e:
            print(f"Error insertando al visitante: {e}")
            return None
    
    @staticmethod
    def mostrar_todos():
        return list(VisitanteModel.select())
            
    @staticmethod
    def buscar_id(id):
        try:
            return VisitanteModel.get(VisitanteModel.id == id)
        except Exception as e:
            print(f"Error buscando el visitante con id {id}: {e}")
            return None
    
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
        
    @staticmethod
    def mostrar_atraccion(atraccion):
        pass
