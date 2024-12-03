#Clase estacionamiento heradado de nodo
from nodo import Nodo
from config import NOMBRE_BD
import sqlite3

class Estacionamiento(Nodo):
    conn = sqlite3.connect(NOMBRE_BD, check_same_thread=False)
    cursor = conn.cursor()
    def __init__(self, id, nombre, latitud, longitud, valoracion, Plaza):
        # constructor de nodo
        super().__init__(id, nombre, latitud, longitud)
        self.valoracion = valoracion
        self.plaza = Plaza

   # Método para verificar si está lleno
    def esta_lleno(self):
        # Consultar el número de plazas disponibles en la base de datos
        self.cursor.execute("SELECT plaza FROM estacionamiento WHERE id = ?", (self.id,))
        plazas = self.cursor.fetchone()
        if plazas:
            return plazas[0] == 0
        return False

    # Método para ocupar una plaza
    def ocupar(self):
        if self.esta_lleno():
            print("No hay plazas disponibles.")
            return False
        # Actualizar la base de datos y restar una plaza
        self.cursor.execute("UPDATE estacionamiento SET plaza = plaza - 1 WHERE id = ? AND plaza > 0", (self.id,))
        self.conn.commit()
        self.plaza -= 1  # Sincronizar el atributo local
        print(f"Plaza ocupada. Plazas restantes: {self.plaza}")
        return True

    # Método para desocupar una plaza
    def desocupar(self):
        # Actualizar la base de datos y sumar una plaza
        self.cursor.execute("UPDATE estacionamiento SET plaza = plaza + 1 WHERE id = ?", (self.id,))
        self.conn.commit()
        self.plaza += 1  # Sincronizar el atributo local
        print(f"Plaza desocupada. Plazas disponibles: {self.plaza}")
        return True

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