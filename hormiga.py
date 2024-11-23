"""- Probabilidad de elegir caminos
P(A) = (F^alfa * (1/D)* beta)/ Total de arriba
F = feromona vecina
D = distancia
alfa = influencia de feromonas
beta = influencia de visibilidad"""
from nodo import Nodo
from arista import Arista
from estacionamiento import Estacionamiento
from config import PESO_OCUPADO
import random

class Hormiga:
    def __init__(self,idInicio,alfa,beta):
        self.nodoActual = Nodo.obtener(idInicio)
        self.origen = Nodo.obtener(idInicio)
        self.Nodos = [] # ruta de nodos menos la de inicio
        self.Arista = [] # ruta de Arista
        self.alfa = alfa
        self.beta = beta
        self.distanciaTotal = 0

    # moverse 0 = vacio, 1 = moviendo, 2 = llego
    def moverse(self, vecinos):
        probabilidades = {} # Diccinario
        total = 0
        for vecino in vecinos:
            if vecino.nodoFinal not in self.Nodos:
                distancia, nodo = vecino.ObtenerDistancia()
                if distancia != PESO_OCUPADO:
                    probabilidad = (vecino.feromonas ** self.alfa)  *  ((1 / distancia) ** self.beta)
                    probabilidades[vecino] = probabilidad
                    total += probabilidad
                    print(f"({vecino.id}) = {probabilidad}")

        if total == 0:
            return 0

        aristaCambio = self.moverseProbablidad(probablidades=probabilidades,total=total)
        self.distanciaTotal += aristaCambio.distancia # aumentar distancia
        self.Arista.append(aristaCambio.id) #guardar arista
        self.nodoActual = Nodo.obtener(aristaCambio.nodoFinal)
        self.Nodos.append(self.nodoActual.id)
        print(f"Se mueve en la arista {aristaCambio.id} a nodo {self.nodoActual.id}")
        if Estacionamiento.obtener(self.nodoActual.id):
            return 2
        return 1

    # moverse con la probabilidad calculada
    def moverseProbablidad(self, probablidades, total):
        numero_random = random.uniform(0, total)
        suma_acumulada = 0
        seleccion = None
        # Sacar el siguente nodo
        for arista, probabilidad in probablidades.items():
            suma_acumulada += probabilidad
            if numero_random <= suma_acumulada:
                seleccion = arista
                break
        return seleccion

    # retorna id de ubicacion actual
    def ubicacionActual(self):
        return self.nodoActual.id
    # regresar al origen
    def resetear(self):
        self.nodoActual = self.origen
        self.Nodos = [] 
        self.Arista = [] 
        self.distanciaTotal = 0