from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.ticket_model import TicketModel
from models.visitante_model import VisitanteModel
import datetime
import json

class TicketRepo:
    @staticmethod
    def crear_ticket(visitante_id, atraccion_id, fecha_compra, fecha_visita, tipo_ticket, usado, fecha_uso, detalles_compra_json=None):
        try:
            if detalles_compra_json:
                return TicketModel.create(visitante_id=visitante_id, atraccion_id=atraccion_id, fecha_compra=fecha_compra, fecha_visita=fecha_visita, tipo_ticket=tipo_ticket, usado=usado, fecha_uso=fecha_uso, detalles_compra=detalles_compra_json)
            else:
                return TicketModel.create(visitante_id=visitante_id, atraccion_id=atraccion_id, fecha_compra=fecha_compra, fecha_visita=fecha_visita, tipo_ticket=tipo_ticket, usado=usado, fecha_uso=fecha_uso)
        except Exception as e:
            print(f"Error insertando el ticket: {e}")
            return None

    @staticmethod
    def mostrar_todos():
        return list(TicketModel.select())
        
    @staticmethod
    def buscar_id(id):
        try:
            return TicketModel.get(TicketModel.id == id)
        except Exception as e:
            print(f"Error buscando el ticket con id {id}: {e}")
            return None
        
    @staticmethod
    def cambiar_precio_ticket(ticket_id, nuevo_precio):
        try:
            ticket = TicketRepo.buscar_id(ticket_id) # buscamos el ticket que quiere cambiar el usuario
            if ticket: # si existe cambiaremos el precio al que ha introducido el usuario
                ticket.detalles_compra["precio"] = nuevo_precio # modificacion del precio almacenado en el jsonb
                ticket.save()
            else:
                print("El ticket introducido no existe")
        except Exception as e:
            print(f"Error al cambiar el precio del ticket: {e}")
            return None

    @staticmethod
    def mostrar_por_visitante(id_visitante):
        return list(TicketModel.select().where(TicketModel.visitante_id==id_visitante))
    
    @staticmethod
    def mostrar_por_atraccion(id_atraccion):    
        return list(TicketModel.select().where(TicketModel.atraccion_id==id_atraccion))
    
    # TERMINAR DE ENTENDER PARA COMPLETAR LA CONSULTA. OBTENER VISITANTES QUE TIENEN UN TICKET PARA UNA ATRACCION (DIRECTA O GENERAL)
    @staticmethod
    def mostrar_ticket_visitantes_atraccion(id_atraccion):
        pass
        #return list(VisitanteModel.select().join(TicketModel).where((TicketModel.atraccion_id=id_atraccion) or (TicketModel.id_atraccion )))
    
    @staticmethod
    def actualizar_uso(id):
        try:
            ticket = TicketRepo.buscar_id(id)
            if not ticket:
                print(f"Ticket {id} no encontrado.")
                return
            
            ticket.usado = True
            ticket.fecha_uso = datetime.now()
            ticket.save()
            print(f"El uso del ticket {id} se ha cambiado a {ticket.usado}")
            return ticket
        except Exception as e:
            print(f"Error al cambiar el estado de uso del ticket {id}: {e}")
            return None