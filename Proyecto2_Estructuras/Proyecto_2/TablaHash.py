
class TablaHash:
    def __init__(self):#Constrictor
        self.tableHash = {}

    
    def funcionHash(self, value):#Constructor con parametros/Crea la llave para poder hacer la insercion
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key 

    def insertTableHash(self, value,valor):#Inserta el elemento usando la llave creada en el metodo funcionHash
        hash = self.funcionHash(value)
        if self.tableHash.get(hash) is None:
            self.tableHash[hash] = valor

    def searchTableHash(self,value): #Busca usando la llave creada en el metodo funcionHash
        hash = self.funcionHash(value);
        if self.tableHash.get(hash) is None:
            return None
        else:
            return self.tableHash[hash]
  

