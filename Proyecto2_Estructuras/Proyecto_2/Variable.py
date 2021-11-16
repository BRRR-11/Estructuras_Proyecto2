
class Variable:
    def __init__(self, tipo,nombre,valor,alcance,linea):
        self.typeVar = tipo
        self.nameVar = nombre
        self.alcance = alcance
        self.valueVar = valor
        self.lineVar = linea

    def getLineVar(self):
        return self.lineVar

    def getTypeVar(self):
        return self.typeVar

    def getNameVar(self):
        return self.nameVar

    def getAlcanceVar(self):
        return self.alcance
    
    def getValueVar(self):
        return self.valueVar

   
