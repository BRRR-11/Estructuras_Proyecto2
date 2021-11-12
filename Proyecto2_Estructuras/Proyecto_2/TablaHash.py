
class TablaHash:
    def __init__(self):
        self.table = {}

    
    def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key 

    def Insert(self, value,valor):
        hash = self.Hash_func(value)
        if self.table.get(hash) is None:
            self.table[hash] = valor

    def Search(self,value): 
        hash = self.Hash_func(value);
        if self.table.get(hash) is None:
            return None
        else:
            return self.table[hash]
  

