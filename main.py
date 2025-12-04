from pprint import pprint
from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from playhouse import shortcuts #type: ignore 
from database import db, inicializar_base
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
from models.ticket_model import TicketModel
from repositories.visitante_repo import VisitanteRepo
from repositories.atraccion_repo import AtraccionRepo
from repositories.ticket_repo import TicketRepo 

inicializar_base([VisitanteModel, AtraccionModel, TicketModel])

