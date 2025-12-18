from pprint import pprint
from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from playhouse import shortcuts #type: ignore 
import datetime
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
        print("\n--> VISITANTES\n" \
        "\n1. Crear visitante\n" \
        "\n2. Mostrar visitantes\n" \
        "\n3. Eliminar visitante\n" \
        "\n4. Mostrar visitantes con preferencia por las atracciones 'extremas'\n" \
        "\n5. Mostrar visitantes con problemas cardiacos\n" \
        "\n0. Volver\n"
        )
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                altura = input("Altura: ")
                preferencias = {}
                VisitanteRepo.crear_visitante(nombre, email, altura)
                print("Visitante creado correctamente.")
            case "2":
                for visitante in VisitanteRepo.mostrar_todos():
                    pprint(visitante.__dict__["__data__"])
            case "3":
                id = int(input("ID del visitante a eliminar: "))
                VisitanteRepo.eliminar_visitante(id)
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
        print("\n--> ATRACCIONES\n" \
            "\n1. Crear atraccion\n" \
            "\n2. Mostrar atracciones\n" \
            "\n3. Eliminar atraccion\n" \
            "\n4. Mostrar atracciones activas\n" \
            "\n5. Mostrar atracciones con intensidad mayor a 7\n" \
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
                AtraccionRepo.eliminar_atraccion(id)
            case "4":
                for atraccion in AtraccionRepo.mostrar_activas():
                    pprint(atraccion.__dict__["__data__"])
            case "5":
                # NO ESTA TERMINADO
                for atraccion in AtraccionRepo.mostrar_intensidad():
                    pprint(atraccion.__dict__["__data__"])
            case "6":
                # NO ESTA TERMINADO
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
    while True:
        print("\n--> TICKETS\n" \
            "\n1. Crear ticket\n" \
            "\n2. Mostrar tickets\n" \
            "\n3. Mostrar tickets de un visitante\n" \
            "\n4. Mostrar tickets de una atraccion\n" \
            "\n5. Mostrar visitantes con ticket para una atraccion (directa o general)\n"\
            "\n6. Marcar ticket como 'usado'\n"\
            "\n7. Mostrar tickets tipo 'colegio' con un precio inferior a 30e\n"\
            "\n8. Mostrar tickets con descuento de 'estudiante'\n"
            "\n0. Volver\n"
        )
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                id_visitante = int(input("ID de visitante: "))
                id_atraccion_str = input("Indica el ID de la atraccion o dejalo vacio si es general: ")
                if id_atraccion_str == "":
                    id_atraccion = None
                else:
                    id_atraccion=int(id_atraccion_str)
                fecha_visita = input("Fecha de visita (YYYY-MM-DD): ")
                tipo_ticket = input("Tipo de ticket (general, colegio o empleado): ")
                usado = False
                fecha_uso = None
                detalles ={}
                TicketRepo.crear_ticket(id_visitante,id_atraccion,fecha_visita,tipo_ticket,usado,fecha_uso,detalles)
                print("Ticket creado correctamente.")
            case "2":
                for ticket in TicketRepo.mostrar_todos():
                    pprint(ticket.__dict__["__data__"])
            case "3":
                id = int(input("ID del visitante: "))
                for ticket in TicketRepo.mostrar_por_visitante(id):
                    pprint(ticket.__dict__["__data__"])
            case "4":
                id = int(input("ID de la atraccion: "))
                for ticket in TicketRepo.mostrar_por_atraccion(id):
                    pprint(ticket.__dict__["__data__"])
            case "5":
                for ticket in TicketRepo.mostrar_ticket_visitantes_atraccion():
                    pprint(ticket.__dict__["__data__"])
            case "6":
                id = int(input("ID del ticket que quieres marcar como usado: "))
                TicketRepo.actualizar_uso(id)
            case "7":
                for ticket in TicketRepo.mostrar_ticket_colegio():
                    pprint(ticket.__dict__["__data__"])
            case "8":
                for ticket in TicketRepo.mostrar_descuento_estudiante():
                    pprint(ticket.__dict__["__data__"])
            case "0":
                break
            case _:
                print("Opcion no valida")
def opjson():
    while True:
        print("\n--> OPERACIONES JSON\n" \
            "\n1. Cambiar precio de un ticket\n" \
            "\n2. Eliminar restriccion a un visitante\n" \
            "\n3. Agregar una nueva caracteristica de una atraccion\n" \
            "\n4. Agregar una nueva visita al historial de visitas de un visitante\n" \
            "\n0. Volver"
        )
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                break
            case "2":
                break
            case "3":
                break
            case "4":
                break
            case "0":
                break
            case _:
                print("Opcion no valida")

def consultas_utiles():
    while True:
        print("\n--> CONSULTAS UTILES\n" \
            "\n1. Mostrar visitantes ordenados por cantidad total de tickets comprados (mayor-menor)\n" \
            "\n2. 5 atracciones mas vendidas (en tickets especificos)\n" \
            "\n3. Visitantes que han gastado mas de 100e en tickets\n" \
            "\n4. Actividades compatibles para un visitante\n" \
            "\n0. Volver"
        )
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                break
            case "2":
                break
            case "3":
                break
            case "4":
                break
            case "0":
                break
            case _:
                print("Opcion no valida")

def main():
    principal()


if __name__ == "__main__":
    inicializar_base([AtraccionModel, VisitanteModel, TicketModel])
    ingesta()
    main()