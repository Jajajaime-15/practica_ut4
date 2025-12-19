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
                tipo_fav = input("Indica si tienes un tipo de atraccion favorita (extrema,familia,infantil,acuatica): ")
                restricciones_txt = input("Indica si tienes algun tipo de restriccion, si es mas de una separa con ',': ")
                restricciones = [] # lista de restricciones 
                if restricciones_txt != "":
                    partes = restricciones_txt.split(",")
                    for restriccion in partes:
                        restriccion = restriccion.strip()
                        if restriccion != "":
                            restricciones.append(restriccion)
                preferencias = None
                if tipo_fav != "" or len(restricciones)>0:
                    preferencias = {
                        "tipo_favorito": tipo_fav,
                        "restricciones": restricciones,
                        "historial_visitas":[]
                    }
                VisitanteRepo.crear_visitante(nombre, email, altura, preferencias)
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
                duracion = input("Duracion en segundos: ")
                capacidad = input("Personas que entran por turno: ")
                intensidad = input("Intensidad de la atraccion de 1 a 10: ")
                caracteristicas = input("Indica si tiene alguna caracteristica (ej. looping, caida libre...), si tiene mas de una separalo con ',': ")
                apertura = input ("Hora de apertura (HH:MM): ")
                cierre = input("Hora cierre (HH:MM):")
                mantenimiento = input("Horarios de mantenimiento (HH:MM-HH:MM), si tiene mas de uno separa por ',': ")
                lista_caracteristicas=[]
                if caracteristicas != "":
                    partes = caracteristicas.split(",")
                    for caracteristica in partes:
                        caracteristica=caracteristica.strip()
                        if caracteristica != "":
                            lista_caracteristicas.append(caracteristica)
                horarios_mante =[]
                if mantenimiento != "":
                    partes_mante = mantenimiento.split(",")
                    for mante in partes_mante:
                        mante = mante.strip()
                        if mante != "":
                            horarios_mante.append(mante)
                detalles = {
                        "duracion_segundos": duracion,
                        "capacidad_por_turno": capacidad,
                        "intensidad": intensidad,
                        "caracteristicas": lista_caracteristicas,
                        "horarios":{
                            "apertura":apertura,
                            "cierre": cierre,
                            "mantenimiento": horarios_mante
                        }
                    }
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
                precio = input("Precio: ")
                descuentos = input("Indica si hay algun descuento aplicado,si hay mas de uno separa por ',': ")
                extras = input("Indica si incluye algun servicio extra, si incluye mas de uno separa por ',': ")
                metodo_pago = input("Indica el metodo de pago: ")
                detalles ={}
                if precio != "":
                    detalles["precio"]= float(precio)
                if descuentos != "":
                    lista_descuentos=[]
                    partes_desc = descuentos.split(",")
                    for descuento in partes_desc:
                        descuento = descuento.strip()
                        if descuento != "":
                            lista_descuentos.append(descuento)
                    detalles["descuentos_aplicados"] = lista_descuentos
                if extras != "":
                    lista_extras = []
                    partes_extras = extras.split(",")
                    for extra in partes_extras:
                        extra = extra.strip()
                        if extra != "":
                            lista_extras.append(extra)
                    detalles["servicios_extra"] = lista_extras
                if metodo_pago != "":
                    detalles["metodo_pago"] = metodo_pago
                TicketRepo.crear_ticket(id_visitante,id_atraccion,fecha_visita,tipo_ticket,detalles)
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
                ticket_id = int(input("ID del ticket al que quieres cambiarle el precio: "))
                nuevo_precio = float(input("Introduce el nuevo precio del ticket (decimal con punto en vez de coma): "))
                TicketRepo.cambiar_precio_ticket(ticket_id, nuevo_precio)
            case "2":
                visitante_id = int(input("ID del visitante al que quieres eliminar una restriccion: "))
                restriccion = input("Introduce el nombre de la restriccion a eliminar (si es mas de una palabra la separacion sera '_'): ")
                VisitanteRepo.eliminar_restriccion_visitante(visitante_id, restriccion)
            case "3":
                atraccion_id = int(input("ID de la atraccion a la que quieras anyadir una caracteristica: "))
                caracteristica = input("Introduce el nombre de la nueva caracteristica: ")
                AtraccionRepo.anyadir_caracteristica_atraccion(atraccion_id, caracteristica)
            case "4":
                visitante_id = int(input("ID del visitante al que quieres agregar una visita: "))
                fecha = input("Fecha de visita (YYYY-MM-DD): ")
                atracciones = int(input("Numero de atracciones visitadas: "))
                visita = {"fecha" : fecha, "atracciones_visitadas" : atracciones}
                VisitanteRepo.anyadir_visita(visitante_id, visita)
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
            "\n4. Atracciones compatibles para un visitante\n" \
            "\n0. Volver"
        )
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1":
                for visitante in VisitanteRepo.visitantes_ordenados_tickets():
                    pprint(visitante.__dict__["__data__"])
                    print(f"Total tickets: {visitante.total_tickets}")
                    #print(f"Nombre: {visitante.nombre} - Tickets comprados: {visitante.total_tickets}")
            case "2":
                for atraccion in AtraccionRepo.atracciones_mas_vendidas():
                    pprint(atraccion.__dict__["__data__"])
                    print(f"Total tickets: {atraccion.total_tickets}")
                    #print(f"Atraccion: {atraccion.id} - Tickets comprados: {atraccion.total_tickets}")
            case "3":
                for visitante in VisitanteRepo.visitantes_gastado_tickets():
                    pprint(visitante.__dict__["__data__"])
                    print(f"Total tickets: {visitante.gasto_total}")
            case "4":
                id = int(input("ID del visitante: "))
                for atraccion in AtraccionRepo.atracciones_compatibles(id):
                    pprint(atraccion.__dict__["__data__"])
            case "0":
                break
            case _:
                print("Opcion no valida")

def main():
    principal() # metodo que contiene el menu principal

if __name__ == "__main__":
    inicializar_base([AtraccionModel, VisitanteModel, TicketModel]) # borramos y creamos las tablas
    ingesta() # introducimos los datos de la ingesta en las tablas
    main() # llamada al metodo principal para ejecutar el programa