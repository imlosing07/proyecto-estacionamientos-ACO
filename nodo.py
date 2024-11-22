#Clase Nodo
import sqlite3

class Nodo:
    def __init__(self, id, nombre, latitud, longitud):
        self.id = id
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud

    # Metodo para obtener un nodo por su ID
    @staticmethod
    def obtener(id):
        conn = sqlite3.connect('base_grafo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nodo WHERE ID = ?", (id,))
        resultado = cursor.fetchone()  # Obtener una fila del resultado
        conn.close()
        
        if resultado:
            return Nodo(id=resultado[0], nombre=resultado[1], latitud=resultado[2], longitud=resultado[3])
        return None
    
    