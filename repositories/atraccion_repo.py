from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.atraccion_model import AtraccionModel
import json

class AtraccionRepo:
    @staticmethod
    def crear_atraccion(nombre, tipo, altura_minima, detalles_json = None):
        try:
            if detalles_json:
                return AtraccionModel.create(nombre=nombre, tipo=tipo, altura_minima=altura_minima, detalles_json=detalles_json)
            else:
                return AtraccionModel.create(nombre=nombre, tipo=tipo, altura_minima=altura_minima, detalles_json=detalles_json)
        except Exception as e:
            print(f"Error insertando la atraccion: {e}")
            return None