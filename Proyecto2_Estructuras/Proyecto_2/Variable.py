
class Variable:
    def __init__(self, tipo,nombre,valor,alcance,linea):
        self.typeVar = tipo
        self.nameVar = nombre
        self.alcance = alcance
        self.valueVar = valor
        self.lineVar = linea

    def getLineVar(self):#Obtine la linea de codigo en la que se encuentra la variable
        return self.lineVar

    def getTypeVar(self):#Obtiene el tipo de variable int,float,string
        return self.typeVar

    def getNameVar(self):#Obtiene el nombre de la varible
        return self.nameVar

    def getAlcanceVar(self):#Global o no global
        return self.alcance
    
    def getValueVar(self):#Obtine el valor de la varible
        return self.valueVar

   
