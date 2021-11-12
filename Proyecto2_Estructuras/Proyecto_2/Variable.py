
class Variable:
    def __init__(self, tipo,nombre,valor,alcance,linea):
        self.tipo = tipo
        self.nombre = nombre
        self.alcance = alcance
        self.valor = valor
        self.linea = linea

    def getLinea(self):
        return self.linea

    def getTipo(self):
        return self.tipo

    def getNombre(self):
        return self.nombre

    def getAlcance(self):
        return self.alcance
    
    def getValor(self):
        return self.valor

   
