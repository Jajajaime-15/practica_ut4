from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.ticket_model import TicketModel
import json

class TicketRepo:
    @staticmethod
    def crear_ticket(visitante_id, fecha_visita, tipo_ticket, detalles_compra_json, atraccion_id):
        pass
