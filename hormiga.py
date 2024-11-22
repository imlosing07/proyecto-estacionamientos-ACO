"""- Probabilidad de elegir caminos
P(A) = (F^alfa * V^beta)/ Total de arriba
F = feromona vecina
V = visibilidad = 1/distancia
alfa = influencia de feromonas
beta = influencia de visibilidad"""
from nodo import Nodo
from arista import Arista

class Hormiga:
    def __init__(self,idInicio,alfa,beta):
        self.nodoActual = Nodo.obtener(idInicio)
        self.Nodos = [] # ruta de nodos
        self.Arista = [] # ruta de Arista
        self.alfa = alfa
        self.beta = beta
        self.distanciaTotal = 0

    # moverse
    def moverse(vecinos):
        print("me muevo en mi sitio")


