from grafo import Grafo
from hormiga import Hormiga
from config import FeromonaDepositida, ITERACION
class ACO(Grafo):
    def __init__(self,idInicio):
        super().__init__()
        self.NodoRapida = [] # guardar mejor camino
        self.AristaRapida = [] 
        self.hormigas = [] # Hormigas = nodos / 2 
        self.menorDistancia = 1000000
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=5,beta=1))
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=5,beta=1))
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=4,beta=4))
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=3,beta=3))
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=2,beta=5))
        self.hormigas.append(Hormiga(idInicio=idInicio,alfa=2,beta=5))

    def ejecutar(self,iteracion=ITERACION):
        if iteracion == 0: # si llega a cero
            print("Nodo")
            print(self.NodoRapida)
            print("Arista")
            print(self.AristaRapida)
            print(f"Menor de {self.menorDistancia:.2f}")
            #self.imprimir() #Eliminar
            return {
                "Nodo":self.NodoRapida,
                "Arista":self.AristaRapida,
                "distancia":f"{self.menorDistancia:.2f}"
            }
        
        #print(f"---------------- {iteracion} iter ----------------") #Eliminar

        for hormiga in self.hormigas:
            resultado = 0
            while (True):
                vecinos = self.buscarVecino(hormiga.ubicacionActual())
                resultado = hormiga.moverse(vecinos) #0 = quedo , 1 = continuar, 2 meta
                if resultado != 1:
                    break
          
            if (resultado == 2):
                """for arista in self.aristas:
                    if arista.id in hormiga.Arista:
                        arista.feromonas += FeromonaDepositida/arista.distancia""" # aumentar la feromona   

                # Guardatos del minimo
                #print(f"Menor de {hormiga.distanciaTotal} y {self.menorDistancia}")#eliminar
                self.menorDistancia = min(hormiga.distanciaTotal, self.menorDistancia)
                if (self.menorDistancia == hormiga.distanciaTotal):
                    self.NodoRapida = hormiga.Nodos # guardar el menor
                    self.AristaRapida = hormiga.Arista
                    for arista in self.aristas:
                        if arista.id in hormiga.Arista:
                            arista.feromonas += (FeromonaDepositida/arista.distancia)*2 # aumentar la feromona 
                else:
                    for arista in self.aristas:
                        if arista.id in hormiga.Arista:
                            arista.feromonas += FeromonaDepositida/arista.distancia # aumentar la feromona 
 
            hormiga.resetear()
        self.evaporar() #evaporar feromonas

        return self.ejecutar(iteracion - 1)
