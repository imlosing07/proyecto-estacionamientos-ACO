from grafo import Grafo
from hormiga import Hormiga
from config import FEROMONA_COLOCAR, ITERACIONES
class ACO:
    def __init__(self,grafo,idOrigen):
        self.grafo = grafo
        self.nodoOrigen = self.grafo.nodos[idOrigen] # nodo de origen
        self.hormigas = []
        self.hormigas.append(Hormiga(nodoInicio=self.nodoOrigen,alfa=1,beta=1)) 
        self.hormigas.append(Hormiga(nodoInicio=self.nodoOrigen,alfa=1,beta=1)) 
        self.hormigas.append(Hormiga(nodoInicio=self.nodoOrigen,alfa=1,beta=1)) 
        self.hormigas.append(Hormiga(nodoInicio=self.nodoOrigen,alfa=1,beta=1)) 

        self.solucion = [] #nodos
        self.distanciaMinima = 1000000

    # buscar el camino
    def ejecutar(self, iteraciones=ITERACIONES):
        while iteraciones > 0:
           
            soluciones = {}
            minimo = 1000000
            nodosMin = []  # Reiniciar nodosMin en cada iteración para evitar acumulación

            for hormiga in self.hormigas: 
                recorrer = 1
                # hasta encontrar el camino
                while recorrer == 1:
                    recorrer = hormiga.mover(self.grafo.buscarVecino(hormiga.ubicacion_actual()))

                # si llegó a un estacionamiento 
                if recorrer == 0:
                    soluciones[hormiga.distancia] = hormiga.Aristas  # guardar el camino recorrido por la hormiga
                    # Ver si es el mínimo
                    if hormiga.distancia < minimo:
                        minimo = hormiga.distancia
                        nodosMin = hormiga.NodosOrdenados  # Aquí se asignan solo los nodos recorridos

                hormiga.resetear()

            if minimo < self.distanciaMinima:
                self.distanciaMinima = minimo
                self.solucion = nodosMin  # Solo actualizar la solución cuando encontramos una mejor

            self.grafo.evaporar()

            # Guardar feromonas        
            for distancia, aristas in soluciones.items():
                for arista in aristas:
                    if distancia == minimo:
                        arista.feromonas += (FEROMONA_COLOCAR / distancia) * 2 
                    else:    
                        arista.feromonas += FEROMONA_COLOCAR / distancia

            iteraciones -= 1  # Decrementamos las iteraciones

        # Después de completar todas las iteraciones, imprime el resultado
        SolucionNodos = {}
        i = 0
        SolucionNodos[i] = self.nodoOrigen.exportJson()
        for sol in self.solucion:
            i += 1
            SolucionNodos[i] = self.grafo.nodos[sol].exportJson()
        
        i += 1
        return {"distancia":self.distanciaMinima,"rutas":SolucionNodos,"nodosTotales":i}