from estacionamiento import Estacionamiento
import sqlite3

NombreBD = 'base_grafo.db'

class Arista:
    def __init__(self, id, nodoInicio, nodoFinal, distancia,feromonas=1.0): #Feromonas = C/(nodosTotales*longuitud)
        self.id = id
        self.nodoInicio = nodoInicio
        self.nodoFinal = nodoFinal
        self.distancia = distancia
        self.feromonas = feromonas
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
        estacionamiento = Estacionamiento.obtener(self.nodoFinal) #Ver sui existe estacionamiento
        if estacionamiento and estacionamiento.esta_lleno():
            del estacionamiento # eliminar
            return 10000, self.nodoFinal # Cambiar la distancia para la solucion 
        else:
            del estacionamiento # eliminar
            return self.distancia, self.nodoFinal