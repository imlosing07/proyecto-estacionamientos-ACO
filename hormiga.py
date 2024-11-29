# Clase hormiga
from arista import Arista
from config import FACTOR_ESCALAR
import random

class Hormiga:
    def __init__(self,nodoInicio,alfa,beta):
        self.nodoActual = nodoInicio
        self.origen = nodoInicio
        self.NodosVisitados = set() #lista de nodos
        self.NodosOrdenados = []
        self.Aristas = [] # ruta de Arista
        self.alfa = alfa
        self.beta = beta
        self.distancia = 0

    # retorna -1 si no encontro ruta
    # retorna 0 si encontro un nodo
    # retorna 1 si encontro el estacionamiento
    def mover(self,vecinos): 
        # sacar probabilidades
        probabilidades = {}
        total = 0
        for arista in vecinos:
            if arista.nodoFinal.id not in self.NodosVisitados:
                probabilidad = (arista.feromonas ** self.alfa) * ((1/(arista.obtenerDistacia()/FACTOR_ESCALAR)) ** self.beta)
                probabilidades[arista] = probabilidad
                total += probabilidad
        if total == 0:
            return -1
        
        arista = self.moverseProbablidad(probabilidades,total)
        # agregar rutas
        self.Aristas.append(arista)
        self.NodosVisitados.add(arista.nodoFinal.id) 
        self.NodosOrdenados.append(arista.nodoFinal.id)
        self.nodoActual = arista.nodoFinal # actualizar ubicacion
        self.distancia += arista.distancia
        #print(f"({arista.id}) Desde {arista.nodoInicio.nombre} Moverse a {arista.nodoFinal.nombre} [{arista.nodoFinal.id}]") # Eliminar
        if(arista.nodoFinal.soyEstacionamiento()):
            #print(f"LLego al estacionamiento ({arista.nodoFinal.id}) {arista.nodoFinal.nombre}")  # Eliminar
            return 0
        else:
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
    
    # regresar al inicio
    def resetear(self):
        self.nodoActual = self.origen
        self.NodosVisitados = set()
        self.NodosOrdenados = []
        self.Arista = []
        self.distancia = 0

    # ubicacion actual
    def ubicacion_actual(self):
        return self.nodoActual.id