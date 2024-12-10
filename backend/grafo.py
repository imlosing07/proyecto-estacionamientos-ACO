# Clase Grafo
from arista import Arista
from nodo import Nodo
from estacionamiento import Estacionamiento
from config import NOMBRE_BD, INDICE_EVAPORACION, FEROMONA_INICIAL
import sqlite3, math

class Grafo:
    def __init__(self):
        self.aristas = {}
        self.nodos = {}
        # Extraer de la base de datos
        conn = sqlite3.connect(NOMBRE_BD) #consultar base de datos
        cursor = conn.cursor()
        # Ejecutar consulta SQL para obtener todos los datos de las aristas
        cursor.execute('SELECT * FROM nodo ')
        resultadosNodos = cursor.fetchall()
        cursor.execute('SELECT * FROM estacionamiento ')
        resultadosEstacionamiento = cursor.fetchall()
        cursor.execute('SELECT * FROM arista ')
        resultadosArista = cursor.fetchall()
        conn.close()
        # sacar estacionamientos
        for registro in resultadosEstacionamiento:
            self.nodos[registro[3]] = [registro[1],registro[2]] #valoracion, plaza

        # sacar nodos
        for registro in resultadosNodos:
            if registro[0] < 1000:
                self.nodos[registro[0]] = Nodo(registro[0],registro[1],registro[2],registro[3])
            else:
                estacionamiento = Estacionamiento(registro[0],registro[1],registro[2],registro[3],self.nodos[registro[0]][0],self.nodos[registro[0]][1])
                self.nodos[registro[0]] = estacionamiento

        # sacar arista 
        for registro in resultadosArista:
            self.aristas[registro[0]] = Arista(registro[0],self.nodos[registro[1]],self.nodos[registro[2]],registro[3])
        
    # evaporar 
    def evaporar(self):
        for arista in self.aristas.values():
            arista.feromonas = arista.feromonas * (1 - INDICE_EVAPORACION)

    # resetear 
    def resetear(self):
        for arista in self.aristas.values():
            arista.feromonas = FEROMONA_INICIAL

    #buscar vecino
    def buscarVecino(self,idNodo):
        Vecinos = []
        for arista in self.aristas.values():
            if (arista.nodoInicio.id == idNodo):
                Vecinos.append(arista)
        return Vecinos # id de aristas
    
    # imprimir estado de feromonas
    def imprimir(self):
        for arista in self.aristas.values():
            print(f"({arista.id}) Feromonas {arista.feromonas}")

    # buscar nodo
    def buscarNodo(self, lat_objetivo, lon_objetivo):
        R = 6371  # Radio 
        distancia_minima = float('inf') 
        nodo_mas_cercano = None  

        lat_objetivo_rad = math.radians(lat_objetivo)
        lon_objetivo_rad = math.radians(lon_objetivo)

        for nodo in self.nodos.values():
            lat_nodo_rad = math.radians(nodo.latitud)
            lon_nodo_rad = math.radians(nodo.longitud)
            lat_diff = lat_nodo_rad - lat_objetivo_rad
            lon_diff = lon_nodo_rad - lon_objetivo_rad
            a = math.sin(lat_diff / 2) ** 2 + math.cos(lat_objetivo_rad) * math.cos(lat_nodo_rad) * math.sin(lon_diff / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distancia = R * c 

            if distancia < distancia_minima:
                distancia_minima = distancia
                nodo_mas_cercano = nodo.id

        return nodo_mas_cercano