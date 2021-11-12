
class Funcion:
    def __init__(self, tipo,nombre,cuerpo,linea):
        self.tipo = tipo
        self.nombre = nombre
        self.cuerpo = cuerpo
        self.linea = linea

    def getlinea(self):
        return self.linea

    def getTipo(self):
        return self.tipo

    def getNombre(self):
        return self.nombre

    def getCuerpo(self):
        return self.cuerpo

   
