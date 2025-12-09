from pprint import pprint
from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from playhouse import shortcuts #type: ignore 
from database import db, inicializar_base
from models.atraccion_model import AtraccionModel
from models.visitante_model import VisitanteModel
from models.ticket_model import TicketModel
from repositories.atraccion_repo import AtraccionRepo
from repositories.ticket_repo import TicketRepo
from repositories.visitante_repo import VisitanteRepo
from ingesta import ingesta

inicializar_base([AtraccionModel, VisitanteModel, TicketModel])
ingesta()

def principal():
    while True:
        print("--> MENU PARQUE DE ATRACCIONES <-- \n"\
            "\n1. Visitantes\n"\
            "\n2. Atracciones\n"\
            "\n3. Tickets\n"\
            "\n4. Operaciones JSON\n"\
            "\n5. Consultas utiles\n"\
            "\n0. Salir\n"
            )
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                while True:
                    print("--> VISITANTES\n" \
                    "\n1. Crear visitante\n" \
                    "\n2. Mostrar visitantes\n" \
                    "\n3. Eliminar visitante\n" \
                    "\n4. Mostrar visitantes con preferencia por las atracciones 'extremas'\n" \
                    "n\5. Mostrar visitantes con problemas cardiacos\n" \
                    "\n0. Volver\n"
                    )
                    opcion = input("Elige una opcion: ")
                    match opcion:
                        case "1":
                            nombre = input("Nombre: ")
                            email = input("Email: ")
                            altura = input("Altura: ")
                            preferencias = "" # MIRAR COMO SE METE JSON
                            VisitanteRepo.crear_visitante(nombre, email, altura)#, preferencias)
                            print("Visitante creado correctamente.")