from grafo import Grafo
from hormiga import Hormiga
from config import FeromonaDepositida
class ACO(Grafo):
    def __init__(self,idInicio):
        super().__init__()
        self.NodoRapida = [] # guardar mejor camino
        self.AristaRapida = [] 
        self.hormigas = [] # Hormigas = nodos / 2 
        self.menorDistancia = 1000000
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=5,beta=2))
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=2,beta=2))
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=2,beta=5))

    def ejecutar(self,iteracion=5):
        if iteracion == 0: # si llega a cero
            print("--------------------------")
            print(self.NodoRapida)
            print(self.AristaRapida)
            return 
        
        for hormiga in self.hormigas:
            print("--------------------------")
            resultado = 0
            while (True):
                vecinos = self.buscarVecino(hormiga.ubicacionActual())
                resultado = hormiga.moverse(vecinos) #0 = quedo , 1 = continuar, 2 meta
                if resultado != 1:
                    break
          
            if (resultado == 2):
                for arista in self.aristas:
                    if arista.id in hormiga.Arista:
                        arista.feromonas += FeromonaDepositida/arista.distancia # aumentar la feromona   

                # Guardatos del minimo
                print(f"Menor de {hormiga.distanciaTotal} y {self.menorDistancia}")
                self.menorDistancia = min(hormiga.distanciaTotal, self.menorDistancia)
                if (self.menorDistancia == hormiga.distanciaTotal):
                    self.NodoRapida = hormiga.Nodos # guardar el menor
                    self.AristaRapida = hormiga.Arista
                    # aumentar la feromona 
                    for arista in self.aristas:
                        if arista.id in hormiga.Arista:
                            arista.feromonas += FeromonaDepositida/arista.distancia # aumentar la feromona 
                    print(hormiga.Arista)
                    print(hormiga.Nodos)
                print(hormiga.distanciaTotal)

            hormiga.resetear()
        self.evaporar() #evaporar feromonas
        self.imprimir()

        self.ejecutar(iteracion - 1)
