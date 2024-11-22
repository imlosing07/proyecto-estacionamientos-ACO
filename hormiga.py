"""- Probabilidad de elegir caminos
P(A) = (F^alfa * V^beta)/ Total de arriba
F = feromona vecina
V = visibilidad = 1/distancia
alfa = influencia de feromonas
beta = influencia de visibilidad"""
from nodo import Nodo
from arista import Arista
import random

class Hormiga:
    def __init__(self,idInicio,alfa,beta):
        self.nodoActual = Nodo.obtener(idInicio)
        self.Nodos = [] # ruta de nodos menos la de inicio
        self.Arista = [] # ruta de Arista
        self.alfa = alfa
        self.beta = beta
        self.distanciaTotal = 0

    # moverse
    def moverse(self, vecinos):
        probabilidades = {} # Diccinario
        total = 0
        for vecino in vecinos:
            probabilidad = (vecino.feromonas ** self.alfa)  *  (1 / vecino.distancia) ** self.beta
            probabilidades[vecino] = probabilidad
            total += probabilidad

        aristaCambio = self.moverseProbablidad(probablidades=probabilidades,total=total)
        self.distanciaTotal += aristaCambio.distancia # aumentar distancia
        self.Arista.append(aristaCambio.id) #guardar arista
        self.nodoActual = Nodo.obtener(aristaCambio.nodoFinal)
        self.Nodos.append(self.nodoActual)
        print(f"Se mueve en la arista {aristaCambio.id} a nodo {self.nodoActual.id}")

    # moverse con la probabilidad calculada
    def moverseProbablidad(self, probablidades, total):
        numero_random = random.uniform(0, total)
        suma_acumulada = 0
        seleccion = None
        # Sacar el siguente nodo
        for nodo, probabilidad in probablidades.items():
            suma_acumulada += probabilidad
            if numero_random <= suma_acumulada:
                seleccion = nodo
                break
        return seleccion

    # retorna id de ubicacion actual
    def ubicacionActual(self):
        return self.nodoActual.id


