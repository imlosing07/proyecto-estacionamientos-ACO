#Probar funciones
"""
Clase Nodo   		ID|Nombre
Clase Estacionamiento	ID|valoracion|Ocupado(true/false)
Clase Arista 		ID|NodoInicio|NodoFinal|Distancia(m)
"""

from nodo import Nodo
from estacionamiento import Estacionamiento
from arista import Arista
from grafo import Grafo
import sqlite3

def crearBaseNodos():
    conn = sqlite3.connect('base_grafo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nodo (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Latitud REAL,
            Longitud REAL
        )
    ''')
    conn.commit()

def insertarNodo(nombre, latitud, longitud):
    conn = sqlite3.connect('base_grafo.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO nodo (Nombre, Latitud, Longitud)
        VALUES (?, ?, ?)
    ''', (nombre, latitud, longitud))
    conn.commit()
    conn.close()

def crearBaseEstacionamiento():
    conn = sqlite3.connect('base_grafo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estacionamiento (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Valoracion INTEGER,
            Plaza INTEGER,
            NodoID INTEGER,
            FOREIGN KEY (NodoID) REFERENCES nodo(ID)
        )
    ''')
    conn.commit()
    conn.close()

def insertarEstacionamiento(nombre, latitud, longitud, valoracion, Plaza):
    conn = sqlite3.connect('base_grafo.db')
    cursor = conn.cursor()
        
    # Insertar en la tabla nodo
    cursor.execute('''
        INSERT INTO nodo (Nombre, Latitud, Longitud)
        VALUES (?, ?, ?)
    ''', (nombre, latitud, longitud))
    
    nodo_id = cursor.lastrowid  # Obtener el ID del nodo recién insertado
    
    # Insertar en la tabla estacionamiento
    cursor.execute('''
        INSERT INTO estacionamiento (Valoracion, Plaza, NodoID)
        VALUES (?, ?, ?)
    ''', (valoracion, Plaza, nodo_id))
    conn.commit()
    conn.close()

def crearArista():
    conn = sqlite3.connect('base_grafo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arista (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NodoInicio INTEGER,
            NodoFinal INTEGER,
            Distancia REAL,
            FOREIGN KEY (NodoInicio) REFERENCES nodo(ID),
            FOREIGN KEY (NodoFinal) REFERENCES nodo(ID)
        )
    ''')
    conn.commit()
    conn.close()

def insertarArista(nodo_inicio, nodo_final, distancia):
    conn = sqlite3.connect('base_grafo.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO arista (NodoInicio, NodoFinal, Distancia)
        VALUES (?, ?, ?)
    ''', (nodo_inicio, nodo_final, distancia))
    conn.commit()
    conn.close()


def Origen():
    crearBaseNodos()
    crearBaseEstacionamiento()
    insertarNodo("nodo1",2.25,2.5)
    insertarNodo("nodo2",2.25,2.5)
    insertarNodo("nodo3",2.25,2.5)
    insertarNodo("nodo4",2.25,2.5)
    insertarNodo("nodo5",2.25,2.5)
    insertarNodo("nodo6",2.25,2.5)
    insertarEstacionamiento("Estacionamiento 1",2.5,2.25,5,2)
    crearArista()
    insertarArista(1,2,5)
    insertarArista(1,3,11)
    insertarArista(2,3,4)
    insertarArista(2,4,3)
    insertarArista(3,1,11)
    insertarArista(3,6,5)
    insertarArista(3,4,10)
    insertarArista(4,5,5)
    insertarArista(5,6,2)
    insertarArista(6,7,1)
    insertarArista(6,3,5)
    insertarArista(7,6,1)


"""a1 = Arista.obtener(10)
a1 = Arista.obtener(9)
distancia , finl = a1.ObtenerDistancia()
print(f"Distancia {distancia}, Final {finl}")
"""
grafo = Grafo()
grafo.buscarVecino(7)

