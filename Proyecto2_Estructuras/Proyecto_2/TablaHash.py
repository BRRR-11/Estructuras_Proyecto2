
class TablaHash:
    def __init__(self):
        self.tableHash = {}

    
    def funcionHash(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key 

    def insertTableHash(self, value,valor):
        hash = self.funcionHash(value)
        if self.tableHash.get(hash) is None:
            self.tableHash[hash] = valor

    def searchTableHash(self,value): 
        hash = self.funcionHash(value);
        if self.tableHash.get(hash) is None:
            return None
        else:
            return self.tableHash[hash]
  

