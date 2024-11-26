"""
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
"""
from fastapi import FastAPI
from pydantic import BaseModel
from config import NombreBD
from ACO import ACO
import sqlite3, math

def obtener_nodo_mas_cercano(lat_objetivo, lon_objetivo):
    R = 6371

    conn = sqlite3.connect(NombreBD)
    cursor = conn.cursor()

    query = "SELECT ID, Latitud, Longitud FROM nodo"
    cursor.execute(query)
    nodos = cursor.fetchall()
    nodo_mas_cercano = None
    distancia_minima = float('inf')
    for nodo in nodos:
        id_nodo, lat_nodo, lon_nodo = nodo

        lat_diff = math.radians(lat_nodo - lat_objetivo)
        lon_diff = math.radians(lon_nodo - lon_objetivo)

        a = math.sin(lat_diff / 2) ** 2 + math.cos(math.radians(lat_objetivo)) * math.cos(math.radians(lat_nodo)) * math.sin(lon_diff / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distancia = R * c  

        if distancia < distancia_minima:
            distancia_minima = distancia
            nodo_mas_cercano = id_nodo
    conn.close()
    return nodo_mas_cercano

#clase para mandar
class Datos(BaseModel):
    nombre: str
    latitud: float
    longitud: float



app = FastAPI()
# metod para construir la api
@app.get("/")
def inicio():
    return {"mensaje": "Bienevenido a la aplicacion"}

# Recepcionar datos
@app.post("/recibir_ruta/")
def retornaRuta(datos: Datos):
    id_Nodo = obtener_nodo_mas_cercano(datos.latitud,datos.longitud)
    Aco = ACO (id_Nodo)
    respuesta  = Aco.ejecutar()
    return respuesta
