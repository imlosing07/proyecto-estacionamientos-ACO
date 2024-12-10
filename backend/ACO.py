from grafo import Grafo  # Importa la clase que representa el grafo.
from hormiga import Hormiga  # Importa la clase que representa una hormiga.
from config import FEROMONA_COLOCAR, ITERACIONES  # Configuración de feromonas y número de iteraciones.

# Clase principal que implementa el algoritmo de optimización por colonia de hormigas (ACO).
class ACO:
    def __init__(self, grafo, idOrigen):
        """
        Constructor de la clase ACO.
        Inicializa el grafo, nodo de origen, lista de hormigas y variables para la solución.
        """
        self.grafo = grafo  # Grafo que se va a recorrer.
        self.nodoOrigen = self.grafo.nodos[idOrigen]  # Nodo inicial a partir del cual las hormigas comienzan.
        
        # Creación de una lista de hormigas que iniciarán desde el nodo de origen.
        self.hormigas = []
        for _ in range(4):  # Se crean 4 hormigas con los mismos parámetros alfa y beta.
            self.hormigas.append(Hormiga(nodoInicio=self.nodoOrigen, alfa=1, beta=1))
        
        self.solucion = []  # Lista que almacenará la mejor ruta encontrada.
        self.distanciaMinima = 1000000  # Distancia inicial muy grande para encontrar la mínima.

    def ejecutar(self, iteraciones=ITERACIONES):
        """
        Ejecuta el algoritmo ACO durante un número específico de iteraciones.
        """
        while iteraciones > 0:
            soluciones = {}  # Diccionario para almacenar las rutas encontradas por las hormigas.
            minimo = 1000000  # Valor mínimo de distancia encontrado en la iteración actual.
            nodosMin = []  # Nodos de la ruta con la distancia mínima.

            # Cada hormiga recorre el grafo buscando rutas.
            for hormiga in self.hormigas:
                recorrer = 1
                while recorrer == 1:
                    # La hormiga se mueve al siguiente nodo basado en las feromonas y la visibilidad.
                    recorrer = hormiga.mover(self.grafo.buscarVecino(hormiga.ubicacion_actual()))
    
                # Si la hormiga llegó a un destino válido (por ejemplo, un estacionamiento).
                if recorrer == 0:
                    # Guarda la distancia recorrida y las aristas visitadas.
                    soluciones[hormiga.distancia] = hormiga.Aristas
                    # Actualiza el mínimo si la ruta encontrada es mejor.
                    if hormiga.distancia < minimo:
                        minimo = hormiga.distancia
                        nodosMin = hormiga.NodosOrdenados  # Guarda los nodos recorridos en la ruta mínima.

                # Reinicia el estado de la hormiga para la próxima iteración.
                hormiga.resetear()

            # Si se encontró una mejor solución, actualiza la solución global.
            if minimo < self.distanciaMinima:
                self.distanciaMinima = minimo
                self.solucion = nodosMin

            # Evapora una parte de las feromonas en todas las aristas del grafo.
            self.grafo.evaporar()

            # Coloca feromonas en las rutas encontradas.
            for distancia, aristas in soluciones.items():
                for arista in aristas:
                    # La mejor ruta recibe más feromonas.
                    if distancia == minimo:
                        arista.feromonas += (FEROMONA_COLOCAR / distancia) * 2
                    else:
                        arista.feromonas += FEROMONA_COLOCAR / distancia

            iteraciones -= 1  # Decrementa el contador de iteraciones.

        # Genera un resultado con la mejor solución encontrada.
        SolucionNodos = {}
        i = 0
        SolucionNodos[i] = self.nodoOrigen.exportJson()  # Exporta el nodo de origen.
        for sol in self.solucion:
            i += 1
            SolucionNodos[i] = self.grafo.nodos[sol].exportJson()  # Exporta cada nodo de la solución.
        
        i += 1
        return {
            "distancia": self.distanciaMinima,  # La distancia total de la mejor ruta.
            "rutas": SolucionNodos,  # La ruta completa en formato JSON.
            "nodosTotales": i  # Número total de nodos en la solución.
        }
