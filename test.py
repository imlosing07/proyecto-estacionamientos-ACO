#Probar funciones
from nodo import Nodo
from estacionamiento import Estacionamiento
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
            Ocupado BOOLEAN,
            NodoID INTEGER,
            FOREIGN KEY (NodoID) REFERENCES nodo(ID)
        )
    ''')
    conn.commit()
    conn.close()

def insertarEstacionamiento(nombre, latitud, longitud, valoracion, ocupado):
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
        INSERT INTO estacionamiento (Valoracion, Ocupado, NodoID)
        VALUES (?, ?, ?)
    ''', (valoracion, ocupado, nodo_id))
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
    insertarEstacionamiento("Estacionamiento 1",2.5,2.25,5,False)

e1 = Estacionamiento.obtener(7)
print(e1.ocupado)