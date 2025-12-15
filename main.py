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
                visitantes()
            case "2":
                atracciones()
            case "3":
                tickets()
            case "4":
                opjson()
            case "5":
                consultas_utiles()
            case "0":
                print("\nSaliendo del programa...")
                break
            case _:
                print("\nOpcion no valida\n")

def visitantes():
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
            case "2":
                for visitante in VisitanteRepo.mostrar_todos():
                    pprint(visitante.__dict__["__data__"])
            case "3":
                id = int(input("ID del visitante a eliminar: "))
                VisitanteRepo.borrar_visitante(id)
                print("Visitante eliminado correctamente")
            case "4":
                for visitante in VisitanteRepo.mostrar_extremas():
                    pprint(visitante.__dict__["__data__"])
            case "5":
                for visitante in VisitanteRepo.mostrar_cardio():
                    pprint(visitante.__dict__["__data__"])
            case "0":
                break
            case _:
                print("Opcion no valida.")

def atracciones():
    while True:
        print("--> ATRACCIONES\n" \
            "\n1. Crear atraccion\n" \
            "\n2. Mostrar atracciones\n" \
            "\n3. Eliminar atraccion\n" \
            "\n4. Mostrar atracciones activas\n" \
            "n\5. Mostrar atracciones con intensidad mayor a 7\n" \
            "\n6. Mostrar atracciones con duracion mayor a 120s\n"\
            "\n7. Mostrar atracciones con 'looping' y 'caida libre'\n"\
            "\n8. Mostrar atracciones con mantenimiento programado\n"\
            "\n9. Cambiar el estado de una atraccion (activa/inactiva)\n"
            "\n0. Volver\n"
        )
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                nombre = input("Nombre: ")
                tipo = input("Tipo: ")
                altura_min = int(input("Altura minima (cm): "))
                detalles = {}
                AtraccionRepo.crear_atraccion(nombre,tipo,altura_min,detalles)
                print("Atraccion creada correctamente.")
            case "2":
                for atraccion in AtraccionRepo.mostrar_todas():
                    pprint(atraccion.__dict__["__data__"])
            case "3":
                id = int(input("ID de la atraccion a eliminar: "))
                AtraccionRepo.eliminar_id(id)
            case "4":
                for atraccion in AtraccionRepo.mostrar_activas():
                    pprint(atraccion.__dict__["__data__"])
            case "5":
                for atraccion in AtraccionRepo.mostrar_intensidad():
                    pprint(atraccion.__dict__["__data__"])
            case "5":
                for atraccion in AtraccionRepo.mostrar_intensidad():
                    pprint(atraccion.__dict__["__data__"])
            case "6":
                for atraccion in AtraccionRepo.mostrar_duracion():
                    pprint(atraccion.__dict__["__data__"])
            case "7":
                for atraccion in AtraccionRepo.mostrar_looping_caida():
                    pprint(atraccion.__dict__["__data__"])
            case "8":
                for atraccion in AtraccionRepo.mostrar_mantenimiento_programado():
                    pprint(atraccion.__dict__["__data__"])
            case "9":
                id = int(input("ID de la atraccion que quieres cambiar el estado: "))
                AtraccionRepo.cambiar_estado(id)
            case "0":
                break
            case _:
                print("Opcion no valida.")

def tickets():
    pass

def opjson():
    pass

def consultas_utiles():
    pass

def main():
    principal()
    VisitanteRepo.crear_visitante()

if __name__ == "__main__":
    inicializar_base([AtraccionModel, VisitanteModel, TicketModel])
    ingesta()
    main()