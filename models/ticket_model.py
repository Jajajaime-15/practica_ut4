from models.base_model import BaseModel
from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
from datetime import datetime

class TicketModel(BaseModel):
    visitante_id = ForeignKeyField(VisitanteModel, backref="tickets")
    atraccion_id = ForeignKeyField(AtraccionModel, backref="tickets", null=True)
    fecha_compra = DateTimeField(default=datetime.now)
    fecha_visita = DateField()
    tipo_ticket = TextField(constraints=[Check("tipo_ticket IN ('general', 'colegio', 'empleado')")])
    detalles_compra = postgres_ext.BinaryJSONField(null=True, default={
        "precio": 45.99,
        "descuentos_aplicados": ["estudiante", "early_bird"],
        "servicios_extra": ["fast_pass", "comida_incluida"],
        "metodo_pago": "tarjeta"
    })
    usado = BooleanField(default=False)
    fecha_uso = DateTimeField(null=True, default=datetime.now)
