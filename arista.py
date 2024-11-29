# Clase arista
from config import FEROMONA_INICIAL, VALOR_DISTANCIA_OCUPADA
class Arista:
    def __init__(self, id, nodoInicio, nodoFinal, distancia): 
        self.id = id
        self.nodoInicio = nodoInicio
        self.nodoFinal = nodoFinal
        self.distancia = distancia
        self.feromonas = FEROMONA_INICIAL

    def obtenerDistacia(self):
        if self.nodoFinal.soyEstacionamiento() and self.nodoFinal.esta_lleno():
            return VALOR_DISTANCIA_OCUPADA
        else:
            return self.distancia