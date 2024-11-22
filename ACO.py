from grafo import Grafo
from hormiga import Hormiga

class ACO(Grafo):
    def __init__(self,idInicio):
        super().__init__()
        self.hormigas = []
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=1,beta=2))

    def ejecutar(self):
        for hormiga in self.hormigas:
            vecinos = self.buscarVecino(hormiga.ubicacionActual())
            hormiga.moverse(vecinos)
            vecinos = self.buscarVecino(hormiga.ubicacionActual())
            hormiga.moverse(vecinos)
            print(hormiga.Nodos)
            print(hormiga.Arista)
