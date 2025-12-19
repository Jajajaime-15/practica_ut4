from models.base_model import BaseModel
from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
from datetime import datetime

class TicketModel(BaseModel):
    visitante_id = ForeignKeyField(VisitanteModel, backref="tickets")
    atraccion_id = ForeignKeyField(AtraccionModel, backref="tickets", null=True)
    fecha_compra = DateTimeField(default=datetime.now) # para que sea la fecha del momento de la creacion si no se especifica
    fecha_visita = DateField()
    tipo_ticket = TextField(constraints=[Check("tipo_ticket IN ('general', 'colegio', 'empleado')")]) 
    detalles_compra = postgres_ext.BinaryJSONField(null=True, default={
        "precio": 0.0,
        "descuentos_aplicados": [],
        "servicios_extra": [],
        "metodo_pago": ""
    })
    usado = BooleanField(default=False) # para que cuente como no usado en caso de que no se diga lo contrario
    fecha_uso = DateTimeField(null=True) # para que se permita no tener fecha de uso, ya que este puede no estar usado
