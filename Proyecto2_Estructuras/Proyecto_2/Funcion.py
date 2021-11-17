
class Funcion:
    def __init__(self, tipo,nombre,contenido,linea):
        self.typeFuncion = tipo
        self.nameFuncion = nombre
        self.contenidoFuncion = contenido
        self.line = linea

    def getlineFuncion(self):
        return self.line

    def getTypeFuncion(self):
        return self.typeFuncion

    def getNameFuncion(self):
        return self.nameFuncion

    def getContenidoFuncion(self):
        return self.contenidoFuncion

   
