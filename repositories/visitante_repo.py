from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.visitante_model import VisitanteModel
from models.ticket_model import TicketModel
from models.atraccion_model import AtraccionModel
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
        
    #Listar visitantes ordenados por cantidad total de tickets comprados    
    @staticmethod
    def visitantes_ordenados_tickets():
        try:
            return list(
                VisitanteModel.select(VisitanteModel.nombre, fn.COUNT(TicketModel.id).alias('total_tickets'))
                .join(TicketModel, on=(VisitanteModel.id == TicketModel.visitante_id))
                .group_by(VisitanteModel.id)
                .order_by(fn.COUNT(TicketModel.id).desc())
            )
        except Exception as e:
            print(f"Error al ordenar los visitantes por tickets comprados: {e}")

    #Obtener visitantes que hayan gastado más de 100€ en tickets (suma de detalles_compra→precio)
    @staticmethod
    def visitantes_gastado_tickets(): 
        try:
            return list(
                VisitanteModel.select(VisitanteModel.nombre, fn.SUM(SQL("CAST(detalles_compra->>'precio' AS DECIMAL)")).alias('gasto_total'))
                  .join(TicketModel, on=(TicketModel.visitante_id == VisitanteModel.id))
                  .group_by(VisitanteModel.id) 
                  .having(SQL("SUM(CAST(detalles_compra->>'precio' AS DECIMAL))") > 10))
        except Exception as e:
            print(f"Error al buscar las atracciones compatibles con el visitante: {e}")
    
    # Modificaciones en jsonb
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
    def anyadir_visita(visitante_id, visita):
        try:
            visitante = VisitanteRepo.buscar_id(visitante_id)
            if visitante: # en caso de existir el visitante introducido
                visitas = visitante.preferencias["historial_visitas"]
                if visita not in visitas: # en caso de no estar la visita en la lista de visitas de la atraccion
                    visitas.append(visita) # anyadiremos la visita a la lista almacenada en el jsonb
                    visitante.preferencias["historial_visitas"] = visitas # asignacion de la lista modificada 
                    visitante.save()
                else:
                    print("La visita indicada ya se encuentra entre las visitas del visitante introducido")
            else:
                print("El visitante introducido no existe")
        except Exception as e:
            print(f"Error al anyadir la visita al visitante: {e}")
            return None