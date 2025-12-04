from database import db
from peewee import * # type: ignore

class BaseModel(Model):
    class Meta:
        database = db