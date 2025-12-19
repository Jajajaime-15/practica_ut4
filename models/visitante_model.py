from models.base_model import BaseModel
from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from datetime import datetime

class VisitanteModel(BaseModel):
    nombre = TextField()
    email = TextField(unique=True)
    altura = IntegerField()
    fecha_registro = DateTimeField(default=datetime.now) # para que sea la fecha del momento de la creacion si no se especifica
    preferencias = postgres_ext.BinaryJSONField(null=True, default={
        "tipo_favorito": "",
        "restricciones": [],
        "historial_visitas": []
    })