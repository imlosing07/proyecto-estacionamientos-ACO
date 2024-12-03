"""
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
"""
from fastapi import FastAPI
from pydantic import BaseModel
from ACO import ACO
from grafo import Grafo


#clase para mandar
class Datos(BaseModel):
    nombre: str
    cordenada: str


app = FastAPI()
grafo = Grafo() # grafo inicializado

# metod para construir la api
@app.get("/")
def inicio():
    return {"mensaje": "Bienevenido a la aplicacion"}

# Recepcionar datos
@app.post("/recibir_ruta/")
def retornaRuta(datos: Datos):
    cordenada = datos.cordenada
    cordenadas = cordenada.split(", ")
    if len(cordenadas) != 2:
        return {"error":"las coordenadas son invalidas"}
    latitud = float(cordenadas[0])
    longitud = float(cordenadas[1])

    idNodo = grafo.buscarNodo(latitud,longitud)
    aco = ACO(grafo,idNodo)
    respuesta  = aco.ejecutar()
    grafo.resetear() # resetear feromonas
    del aco #eliminar objeto
    return respuesta
