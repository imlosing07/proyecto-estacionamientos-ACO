#Clase estacionamiento heradado de nodo
from nodo import Nodo

class Estacionamiento(Nodo):
    def __init__(self, id, nombre, latitud, longitud, valoracion, Plaza):
        # constructor de nodo
        super().__init__(id, nombre, latitud, longitud)
        self.valoracion = valoracion
        self.plaza = Plaza

    # Metodo para ver si esta lleno
    def esta_lleno(self):
        return self.plaza == 0
    # Ocupar (Mejorar para registrar usuario)
    def ocupar(self):
        if self.plaza == 0:
            return False
        self.plaza -= 1
        return True
    # desocupar  (Mejorar para eliminar usuario)
    def desocupar(self):
        self.plaza += 1

    def exportJson(self):
        # Devolver un diccionario con todos los atributos de la clase
        return {
            "id": self.id,
            "nombre": self.nombre,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "valoracion": self.valoracion,
            "plaza": self.plaza
        }

    def soyEstacionamiento(self):
        return True