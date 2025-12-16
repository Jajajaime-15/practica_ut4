from models.base_model import BaseModel
from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from datetime import datetime

class VisitanteModel(BaseModel):
    nombre = TextField()
    email = TextField(unique=True)
    altura = IntegerField()
    fecha_registro = DateTimeField(default=datetime.now)
    preferencias = postgres_ext.BinaryJSONField(null=True, default={
        "tipo_favorito": "extrema",
        "restricciones": ["problemas_cardiacos"],
        "historial_visitas": [
            {"fecha": "2024-06-15", "atracciones_visitadas": 8},
            {"fecha": "2024-08-20", "atracciones_visitadas": 12}
        ]
    })