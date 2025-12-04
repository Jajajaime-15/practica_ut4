from peewee import * #type: ignore
from playhouse import postgres_ext #type: ignore
from models.visitante_model import VisitanteModel
import json

class VisitanteRepo:
    @staticmethod
    def crear_visitante(nombre, email, altura, fecha_registro, preferencias_json=None):
        try:
            if preferencias_json:
                return VisitanteModel.create(nombre=nombre, email=email, altura=altura, fecha_registro=fecha_registro, preferencias_json=preferencias_json)
            else:
                return VisitanteModel.create(nombre=nombre, email=email, altura=altura, fecha_registro=fecha_registro,)
        except Exception as e:
            print(f"Error insertando al visitante: {e}")
            return None