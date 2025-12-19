from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.base_model import BaseModel
from datetime import datetime

class AtraccionModel(BaseModel):
    nombre = CharField(max_length=20, unique = True)
    tipo =CharField(max_length= 30, constraints=[Check("tipo IN ('extrema', 'familiar', 'infantil', 'acuatica')")])
    altura_minima = IntegerField()
    detalles= postgres_ext.BinaryJSONField(default={
        "duracion_segundos" : 30, # por defecto 30s
        "capacidad_por_turno" : 20, # por defecto 20 personas por turno
        "intensidad" : 1,
        "caracteristicas" : [],
        "horarios" : {
            "apertura" : "12:00", # hora de apertura por defecto la hora a la que abre el parque
            "cierre" : "23:00", # hora de cierr por defecto la hora a la que cierra el parque
            "mantenimiento" : ["10:00-11:00"], # por defecto tiene minimo el mantenimiento de antes de abrir el parque
        }
    })
    activa = BooleanField(default=True) # para que cuente como activa en caso de que no se diga lo contrario
    fecha_inauguracion = DateField(default = datetime.now) # para que sea la fecha del momento de la creacion si no se especifica
