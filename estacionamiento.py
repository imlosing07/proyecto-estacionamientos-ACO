from nodo import Nodo
import sqlite3

class Estacionamiento(Nodo):
    def __init__(self, id, nombre, latitud, longitud, valoracion, Plaza):
        # constructor de nodo
        super().__init__(id, nombre, latitud, longitud)
        self.valoracion = valoracion
        self.plaza = Plaza

    # Método para obtener un estacionamiento por su ID
    @staticmethod
    def obtener(id):
        conn = sqlite3.connect('base_grafo.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT nodo.ID, nodo.Nombre, nodo.Latitud, nodo.Longitud, estacionamiento.Valoracion, estacionamiento.Plaza
            FROM nodo
            JOIN estacionamiento ON nodo.ID = estacionamiento.NodoID
            WHERE nodo.ID = ?

        ''', (id,))
        resultado = cursor.fetchone()  # Obtener una fila del resultado
        conn.close()

        if resultado:
            # Crear un objeto Estacionamiento con los datos de la base de datos
            return Estacionamiento(
                id=resultado[0], 
                nombre=resultado[1], 
                latitud=resultado[2], 
                longitud=resultado[3], 
                valoracion=resultado[4], 
                Plaza=resultado[5]
            )
        return None
    
    def esta_lleno(self):
        return self.plaza == 0