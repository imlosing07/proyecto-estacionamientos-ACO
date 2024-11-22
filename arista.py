from estacionamiento import Estacionamiento
import sqlite3

class Arista:
    def __init__(self, id, nodoInicio, nodoFinal, distancia,feromonas):
        self.id = id
        self.nodoInicio = nodoInicio
        self.nodoFinal = nodoFinal
        self.distancia = distancia
        self.feromonas = feromonas
    # Metodo para obtener una Arista por su ID
    @staticmethod
    def obtener(id,Feromonas=0): #Cambiar el predeterminado
        conn = sqlite3.connect('base_grafo.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT arista.ID, arista.NodoInicio, arista.NodoFinal, arista.Distancia,
                   nodo_inicio.Nombre AS NodoInicioNombre, nodo_final.Nombre AS NodoFinalNombre
            FROM arista
            JOIN nodo AS nodo_inicio ON arista.NodoInicio = nodo_inicio.ID
            JOIN nodo AS nodo_final ON arista.NodoFinal = nodo_final.ID
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
        estacionamiento = Estacionamiento.obtener(self.nodoFinal)
        if estacionamiento and estacionamiento.esta_lleno():
            return 10000, self.nodoFinal # Cambiar a infinito un peso 
        else:
            return self.distancia, self.nodoFinal