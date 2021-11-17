
class Funcion:
    def __init__(self, tipo,nombre,contenido,linea):#Constructor
        self.typeFuncion = tipo
        self.nameFuncion = nombre
        self.contenidoFuncion = contenido
        self.line = linea

    def getNameFuncion(self):#Recupera el nombre de la funcion
        return self.nameFuncion

    def getContenidoFuncion(self):#Recupera el contenido la funcion 
        return self.contenidoFuncion

    def getlineFuncion(self):#Obtiene la linea donde se encuentre la funcion
        return self.line

    def getTypeFuncion(self):#Obtiene el tipo de funcion 
        return self.typeFuncion



   
