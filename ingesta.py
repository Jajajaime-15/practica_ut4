from models.visitante_model import VisitanteModel
from models.atraccion_model import AtraccionModel
from models.ticket_model import TicketModel

def ingesta():
    # creacion de 5 visitantes variados
    visitantes_data = [
        {
            "nombre": "Laura Sánchez Pérez",
            "email": "laura.sanchez@email.com",
            "altura": 165,
            "fecha_registro": "2024-01-15 10:30:00",
            "preferencias": {
                "tipo_favorito": "acuatica",
                "restricciones": [],
                "historial_visitas": [
                    {"fecha": "2024-01-20", "atracciones_visitadas": 5},
                    {"fecha": "2024-02-10", "atracciones_visitadas": 7},
                ],
            },
        },
        {
            "nombre": "Miguel Ángel Fernández",
            "email": "miguel.fernandez@email.com",
            "altura": 178,
            "fecha_registro": "2024-01-20 14:15:00",
            "preferencias": {
                "tipo_favorito": "extrema",
                "restricciones": [],
                "historial_visitas": [
                    {"fecha": "2024-01-25", "atracciones_visitadas": 10},
                    {"fecha": "2024-02-15", "atracciones_visitadas": 15},
                ],
            },
        },
        {
            "nombre": "Isabel Rodríguez Torres",
            "email": "isabel.rt@empresa.com",
            "altura": 162,
            "fecha_registro": "2024-02-05 09:00:00",
            "preferencias": {
                "tipo_favorito": "familiar",
                "restricciones": ["embarazo"],
                "historial_visitas": [
                    {"fecha": "2024-02-12", "atracciones_visitadas": 6},
                ],
            },
        },
        {
            "nombre": "David Chen",
            "email": "david.chen@email.com",
            "altura": 180,
            "fecha_registro": "2024-02-10 16:45:00",
            "preferencias": {
                "tipo_favorito": "extrema",
                "restricciones": [],
                "historial_visitas": [
                    {"fecha": "2024-02-18", "atracciones_visitadas": 12},
                    {"fecha": "2024-03-05", "atracciones_visitadas": 18},
                    {"fecha": "2024-03-20", "atracciones_visitadas": 14},
                ],
            },
        },
        {
            "nombre": "Elena Morales Gutiérrez",
            "email": "elena.morales@email.com",
            "altura": 170,
            "fecha_registro": "2024-02-15 11:20:00",
            "preferencias": {
                "tipo_favorito": "extrema",
                "restricciones": ["problemas_cardiacos", "vertigo"],
                "historial_visitas": [
                    {"fecha": "2024-02-22", "atracciones_visitadas": 4},
                    {"fecha": "2024-03-08", "atracciones_visitadas": 5},
                ],
            },
        },
    ]

    # creacion de 5 atracciones variadas
    atracciones_data = [
        {
            "nombre": "Dragón de Fuego",
            "tipo": "extrema",
            "altura_minima": 150,
            "detalles": {
                "duracion_segundos": 150,
                "capacidad_por_turno": 20,
                "intensidad": 9,
                "caracteristicas": ["caida_libre", "giro_360", "looping"],
                "horarios": {
                    "apertura": "10:00",
                    "cierre": "22:00",
                    "mantenimiento": ["13:00-14:00"],
                },
            },
            "activa": True,
            "fecha_inauguracion": "2023-05-15",
        },
        {
            "nombre": "Tobogán Acuático",
            "tipo": "acuatica",
            "altura_minima": 120,
            "detalles": {
                "duracion_segundos": 45,
                "capacidad_por_turno": 30,
                "intensidad": 5,
                "caracteristicas": ["tobogan_curvo", "piscina_final"],
                "horarios": {
                    "apertura": "11:00",
                    "cierre": "20:00",
                    "mantenimiento": ["15:30-16:00"],
                },
            },
            "activa": True,
            "fecha_inauguracion": "2023-06-20",
        },
        {
            "nombre": "Puente Acuático",
            "tipo": "acuatica",
            "altura_minima": 120,
            "detalles": {
                "duracion_segundos": 45,
                "capacidad_por_turno": 30,
                "intensidad": 5,
                "caracteristicas": ["puente_curvo", "piscina_final"],
                "horarios": {
                    "apertura": "11:00",
                    "cierre": "20:00",
                    "mantenimiento": ["15:30-16:00"],
                },
            },
            "activa": True,
            "fecha_inauguracion": "2023-06-20",
        },
        {
            "nombre": "Carrousel Mágico",
            "tipo": "familiar",
            "altura_minima": 90,
            "detalles": {
                "duracion_segundos": 180,
                "capacidad_por_turno": 40,
                "intensidad": 3,
                "caracteristicas": ["caballos_musicales", "luces_led"],
                "horarios": {
                    "apertura": "10:00",
                    "cierre": "21:00",
                    "mantenimiento": [],
                },
            },
            "activa": True,
            "fecha_inauguracion": "2023-04-10",
        },
        {
            "nombre": "Torre del Terror",
            "tipo": "extrema",
            "altura_minima": 140,
            "detalles": {
                "duracion_segundos": 90,
                "capacidad_por_turno": 16,
                "intensidad": 8,
                "caracteristicas": ["caida_libre", "aceleracion_rapida"],
                "horarios": {
                    "apertura": "11:00",
                    "cierre": "23:00",
                    "mantenimiento": ["14:30-15:30"],
                },
            },
            "activa": False,
            "fecha_inauguracion": "2022-08-05",
        },
        {
            "nombre": "Castillo Saltarín",
            "tipo": "infantil",
            "altura_minima": 100,
            "detalles": {
                "duracion_segundos": 300,
                "capacidad_por_turno": 25,
                "intensidad": 2,
                "caracteristicas": ["trampolines", "pelotero", "toboganes_suaves"],
                "horarios": {
                    "apertura": "10:00",
                    "cierre": "19:00",
                    "mantenimiento": ["12:30-13:00"],
                },
            },
            "activa": True,
            "fecha_inauguracion": "2024-01-12",
        },
    ]

    # creacion de 5 tickets variados
    tickets_data = [
        {
            "visitante_id": 1,  # Laura
            "atraccion_id": 1,  # Dragón de Fuego
            "fecha_compra": "2024-01-18 09:15:00",
            "fecha_visita": "2024-01-20",
            "tipo_ticket": "general",
            "detalles_compra": {
                "precio": 50.99,
                "descuentos_aplicados": ["early_bird"],
                "servicios_extra": ["fast_pass"],
                "metodo_pago": "tarjeta",
            },
            "usado": True,
            "fecha_uso": "2024-01-20 11:30:00",
        },
        {
            "visitante_id": 1,
            "atraccion_id": 2,  # Tobogán Acuático
            "fecha_compra": "2024-02-08 14:20:00",
            "fecha_visita": "2024-02-10",
            "tipo_ticket": "general",
            "detalles_compra": {
                "precio": 35.50,
                "descuentos_aplicados": [],
                "servicios_extra": [],
                "metodo_pago": "paypal",
            },
            "usado": True,
            "fecha_uso": "2024-02-10 15:45:00",
        },
        {
            "visitante_id": 2,  # Miguel
            "atraccion_id": 1,
            "fecha_compra": "2024-01-22 16:30:00",
            "fecha_visita": "2024-01-25",
            "tipo_ticket": "general",
            "detalles_compra": {
                "precio": 60.00,
                "descuentos_aplicados": [],
                "servicios_extra": ["fast_pass", "foto_recuerdo"],
                "metodo_pago": "tarjeta",
            },
            "usado": True,
            "fecha_uso": "2024-01-25 12:15:00",
        },
        {
            "visitante_id": 3,  # Isabel
            "atraccion_id": 3,  # Carrousel
            "fecha_compra": "2024-02-08 11:10:00",
            "fecha_visita": "2024-02-12",
            "tipo_ticket": "general",
            "detalles_compra": {
                "precio": 25.00,
                "descuentos_aplicados": ["embarazada"],
                "servicios_extra": [],
                "metodo_pago": "tarjeta",
            },
            "usado": True,
            "fecha_uso": "2024-02-12 10:30:00",
        },
        {
            "visitante_id": 4,  # David
            "atraccion_id": None,  
            "fecha_compra": "2024-03-01 09:00:00",
            "fecha_visita": "2024-03-10",
            "tipo_ticket": "colegio",
            "detalles_compra": {
                "precio": 25.00,
                "descuentos_aplicados": ["estudiante"],
                "servicios_extra": [],
                "metodo_pago": "tarjeta",
            },
            "usado": False,
            "fecha_uso": None,
        },
    ]

    # se realizan las inserciones de todos los visitantes, atracciones y tickets
    VisitanteModel.insert_many(visitantes_data).execute()
    AtraccionModel.insert_many(atracciones_data).execute()
    TicketModel.insert_many(tickets_data).execute()