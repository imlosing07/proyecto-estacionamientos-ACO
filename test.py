from grafo import Grafo
from ACO import ACO
grafo = Grafo()
idNodo = grafo.buscarNodo(-16.392751,-71.537151)
a1 = ACO(grafo,idNodo)
rpta = a1.ejecutar()
print(rpta)