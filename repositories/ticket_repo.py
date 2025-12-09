from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.ticket_model import TicketModel
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
