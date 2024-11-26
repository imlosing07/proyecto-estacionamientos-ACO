"""
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
"""
from fastapi import FastAPI

app = FastAPI()
# metod para construir la api
@app.get("/")
def inicio():
    return {"mensaje": "¡Hola Mundo!"}
