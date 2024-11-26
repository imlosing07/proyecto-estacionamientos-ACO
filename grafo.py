"""
- Evaporacion de feromonas 
F = (1-p) * F
1 = favorece exploracion
0 = favorece explotacion
- Deposito de feromonas 
F = F + Q / distancia
"""
from arista import Arista
from config import NombreBD, IndiceFeromona, INDICE_EVAPORACION
import sqlite3

class Grafo:
    def __init__(self):
        self.aristas = []
        conn = sqlite3.connect(NombreBD)
        cursor = conn.cursor()

        # Ejecutar consulta SQL para obtener todos los datos de las aristas
        cursor.execute('''
            SELECT arista.ID, arista.NodoInicio, arista.NodoFinal, arista.Distancia
            FROM arista
        ''')

        resultados = cursor.fetchall()
        conn.close()

        for registro in resultados:
            self.aristas.append(Arista(
                id=registro[0], 
                nodoInicio=registro[1], 
                nodoFinal=registro[2], 
                distancia=registro[3]
            ))
    # Evopora las feromonas
    def evaporar(self):
        for arista in self.aristas:
            arista.feromonas = arista.feromonas * (1 - INDICE_EVAPORACION)
            
    # resetear feromonas
    def resetear(self):
        for arista in self.aristas:
            arista.feromonas = IndiceFeromona

    # Buscar vecino 
    def buscarVecino(self, idNodo):
        conn = sqlite3.connect(NombreBD)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT arista.ID, arista.NodoInicio, arista.NodoFinal, arista.Distancia
            FROM arista
            WHERE arista.NodoInicio = ?
        ''', (idNodo,))

        resultados = cursor.fetchall()
        conn.close()
        Vecinos = []
        for registro in resultados:
            Vecinos.append(Arista(
                id=registro[0], 
                nodoInicio=registro[1], 
                nodoFinal=registro[2], 
                distancia=registro[3]
            ))
        return Vecinos

    # imprimir la distancia y nodo Final
    def imprimir(self):
        for arista in self.aristas:
            distancia, nodo = arista.ObtenerDistancia()
            print(f"({arista.id}) La distancia {distancia}, nodo Final {nodo} y feromonas {arista.feromonas}") #Eliminar
