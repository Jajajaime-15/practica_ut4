from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.ticket_model import TicketModel
import json

class TicketRepo:
    @staticmethod
    def crear_ticket(visitante_id, atraccion_id, fecha_compra, fecha_visita, tipo_ticket, usado, fecha_uso, detalles_compra_json=None):
        try:
            if detalles_compra_json:
                return TicketModel.create(visitante_id=visitante_id, atraccion_id=atraccion_id, fecha_compra=fecha_compra, fecha_visita=fecha_visita, tipo_ticket=tipo_ticket, usado=usado, fecha_uso=fecha_uso, detalles_compra_json=detalles_compra_json)
            else:
                return TicketModel.create(visitante_id=visitante_id, atraccion_id=atraccion_id, fecha_compra=fecha_compra, fecha_visita=fecha_visita, tipo_ticket=tipo_ticket, usado=usado, fecha_uso=fecha_uso)
        except Exception as e:
            print(f"Error insertando el ticket: {e}")
            return None
