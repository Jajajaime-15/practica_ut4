from pprint import pprint
from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from playhouse import shortcuts #type: ignore 
from database import db, inicializar_base


inicializar_base([])