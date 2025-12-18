from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.base_model import BaseModel
from datetime import datetime

class AtraccionModel(BaseModel):
    nombre = CharField(max_length=20, unique = True)
    tipo =CharField(max_length= 30, constraints=[Check("tipo IN ('extrema', 'familiar', 'infantil', 'acuatica')")])
    altura_minima = IntegerField()
    detalles= postgres_ext.BinaryJSONField(default={
        "duracion_segundos" : 60,
        "capacidad_por_turno" : 24,
        "intensidad" : 8,
        "caracteristicas" : ["looping","caida_libre","giro_360"],
        "horarios" : {
            "apertura" : "10:00",
            "cierre" : "22:00",
            "mantenimiento" : ["14:00-15:00"],
        }
    })
    activa = BooleanField(default=True) # para que cuente como activa en caso de que no se diga lo contrario
    fecha_inauguracion = DateField(default = datetime.now) # para que sea la fecha del momento de la creacion si no se especifica
