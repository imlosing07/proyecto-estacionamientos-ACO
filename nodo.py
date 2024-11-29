# Clase nodo 
class Nodo:
    def __init__(self, id, nombre, latitud, longitud):
        self.id = id
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud


    def exportJson(self):
        return {"id":self.id,"nombre":self.nombre,"latitud":self.latitud,"longitud":self.longitud}
    
    def soyEstacionamiento(self):
        return False