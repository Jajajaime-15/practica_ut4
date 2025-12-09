from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
from models.ticket_model import TicketModel

def ingesta():
    visitantes_data = [
                    # EJEMPLO HAY QUE CAMBIARLOS
                    {
                        'nombre': 'Ana García López',
                        'email': 'ana.garcia@email.com',
                        'altura': '666123456',
                        'fecha_registro': 'particular',
                        'preferencias': {}
                    },
                    {
                        'nombre': 'Carlos Martínez Ruiz',
                        'email': 'carlos.martinez@email.com',
                        'altura': '123',
                        'fecha_registro': 'particular',
                        'preferencias': {}
                    }
                ]

    atracciones_data = [
                    # EJEMPLO HAY QUE CAMBIARLOS
                    {
                        'nombre': 'Ana García López',
                        'tipo': 'ana.garcia@email.com',
                        'altura_minima': '666123456',
                        'detalles': {},
                        'activa': 'ana.garcia@email.com',
                        'fecha_inauguracion': '666123456'
                    },
                    {
                        'nombre': 'Ana García López',
                        'tipo': 'ana.garcia@email.com',
                        'altura_minima': '666123456',
                        'detalles': {},
                        'activa': 'ana.garcia@email.com',
                        'fecha_inauguracion': '666123456'
                    }
                ]

    tickets_data = [
                    # EJEMPLO HAY QUE CAMBIARLOS
                    {
                        'visitante_id': 'Ana García López',
                        'atraccion_id': 'ana.garcia@email.com',
                        'fecha_compra': '666123456',
                        'fecha_visita': 'particular',
                        'tipo_ticket': 'particular',
                        'detalles_compra': {},
                        'usado': 'particular',
                        'fecha_uso': 'particular'
                    },
                    {
                        'visitante_id': 'Ana García López',
                        'atraccion_id': 'ana.garcia@email.com',
                        'fecha_compra': '666123456',
                        'fecha_visita': 'particular',
                        'tipo_ticket': 'particular',
                        'detalles_compra': {},
                        'usado': 'particular',
                        'fecha_uso': 'particular'
                    }
                ]

    VisitanteModel.insert_many(visitantes_data).execute()
    AtraccionModel.insert_many(atracciones_data).execute()
    TicketModel.insert_many(tickets_data).execute()