"""
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
"""
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ACO import ACO
from grafo import Grafo
from typing import Any, Optional

#clase para mandar
class Datos(BaseModel):
    nombre: str
    cordenada: str
    tipo: Optional[str] = None

class User(BaseModel):
    nombre: str

app = FastAPI()
grafo = Grafo() # grafo inicializado
estados = {}

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)
# metod para construir la api
@app.get("/")
def inicio():
    return {"mensaje": "Bienevenido a la aplicacion"}
    
@app.options("/recibir_ruta/")
def handle_options():
    return {"allow": "POST"}
# Recepcionar datos
@app.post("/recibir_ruta/")
def retornaRuta(datos: Datos) -> Any:
    if (datos.nombre in estados) :
        if (datos.tipo != "cambio"):
            return {"error":f"El usuario {datos.nombre} no puede pedir ruta si ya solicito"}
        else:
            grafo.nodos[estados[datos.nombre]].desocupar()
            json_rpta = grafo.nodos[estados[datos.nombre]].exportJson()
            del estados[datos.nombre]
    cordenada = datos.cordenada
    cordenadas = cordenada.split(", ")
    if len(cordenadas) != 2:
        return {"error":"las coordenadas son invalidas"}
    respuesta = solicitarRuta(cordenadas, datos.nombre)
    if (datos.tipo == "cambio"):
        respuesta["success"] = "Se hizo cambio de la ruta"
    return respuesta

@app.post("/liberar_ruta/")
def liberar_ruta(usuario: User):
    if usuario.nombre in estados:
        grafo.nodos[estados[usuario.nombre]].desocupar()
        json_rpta = grafo.nodos[estados[usuario.nombre]].exportJson()
        del estados[usuario.nombre]
        return {"success":"Se libero la ruta ","estacionamiento":json_rpta}
    else:
        return {"error":f"El usuario {usuario.nombre} no tiene solicitudes de ruta pendientes"}
    

def solicitarRuta(cordenadas, nombre):
    latitud = float(cordenadas[0])
    longitud = float(cordenadas[1])
    idNodo = grafo.buscarNodo(latitud,longitud)
    aco = ACO(grafo,idNodo)
    respuesta  = aco.ejecutar()
    id_estacionamiento = respuesta["rutas"][respuesta["nodosTotales"]-1]["id"]
    estados[nombre] = id_estacionamiento
    grafo.resetear() # resetear feromonas
    del aco #eliminar objeto
    return respuesta