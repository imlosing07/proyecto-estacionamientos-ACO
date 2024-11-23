from estacionamiento import Estacionamiento
from config import NombreBD, IndiceFeromona, PESO_OCUPADO
import sqlite3

class Arista:
    def __init__(self, id, nodoInicio, nodoFinal, distancia): 
        self.id = id
        self.nodoInicio = nodoInicio
        self.nodoFinal = nodoFinal
        self.distancia = distancia
        self.feromonas = IndiceFeromona
    # Metodo para obtener una Arista por su ID
    @staticmethod
    def obtener(id): #Cambiar el predeterminado
        conn = sqlite3.connect(NombreBD)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT arista.ID, arista.NodoInicio, arista.NodoFinal, arista.Distancia
            FROM arista
            WHERE arista.ID = ?
        ''', (id,))

        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return Arista(
                id=resultado[0], 
                nodoInicio=resultado[1], 
                nodoFinal=resultado[2], 
                distancia=resultado[3]
            )
        return None
    #retorna distancia, nodoFinal
    def ObtenerDistancia(self):
        estacionamiento = Estacionamiento.obtener(self.nodoFinal) #Ver si existe estacionamiento
        if estacionamiento and estacionamiento.esta_lleno():
            del estacionamiento # eliminar
            return PESO_OCUPADO, self.nodoFinal # Cambiar la distancia para la solucion 
        else:
            del estacionamiento # eliminar
            return self.distancia, self.nodoFinal