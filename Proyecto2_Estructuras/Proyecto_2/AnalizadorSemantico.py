import re
import TablaHash
import Funcion
import Variable


class AnalizadorSemantico:
    def __init__(self):
        self.table = TablaHash.TablaHash()
        self.tokens = ['void','int','float','string']
        

    def search(self,num):
        return self.table.Search(num)
        

    def isFuncion(self,line):
        y = re.search('\(',line)
        if(y):  
            return True
        else:
            return False

    def createTable(self):
        cont = 0
        contenido = ""
        booleana = bool(0)
        cont2 = 0

        with open("codigo.txt", "r") as f:
            for line in f:
                if self.isFuncion(line) is True:
                     name = line.split(' ')[1].strip() 
                     cont = cont + 1
                     contenido = ""
                     for line2 in f:
                         if line2 != ' ':
                            x = re.search('\{',line2)
                            y = re.search('\}',line2)
                            if(x):
                                z = re.search(name,line2)
                                if (z):
                                    cont = cont + 1
                                    cont2 = cont2 + 1
                                else:
                                    if(self.tieneParametros(line) == True):
                                        x1 = 3
                                        while x1 < line.count(" ") - 1:
                                            if  line.split(' ')[x1].strip() != ',':
                                                typeV = line.split(' ')[x1].strip()
                                            if  line.split(' ')[x1+1].strip() != ',':
                                                nameV = line.split(' ')[x1+1].strip()
                                            var = Variable.Variable(typeV,nameV,None,"local",self.numlines(line2))
                                            self.table.Insert(nameV,var)
                                            x1 = x1 + 3
                                 
                                    contenido = contenido + line2
                                    cont = cont+1
                                    cont2 = cont2 + 1
                                 
                                    for i in range(len(self.tokens)):
                                        if line2.split(' ')[0].strip() == self.tokens[i]:
                                            type3 = line2.split(' ')[0].strip()
                                            name3 = line2.split(' ')[1].strip()
                                            if type3 == "int":
                                                valor13 = line2.split('=')[1].strip()
                                                valor3 = valor13.replace(';','')
                                            
                                            var = var.var(type3,name3,valor3,"local",self.numlines(line2))
                                            self.table.Insert(name3,var)
                            else:
                                if(y):
                                    cont = cont-1
                                    if(cont == 0): 
                                        break
                                    contenido = contenido + line2
                                    cont2 = cont2 + 1

                                    for i in range(len(self.tokens)):
                                        if line2.split(' ')[0].strip() == self.tokens[i]:
                                            type3 = line2.split(' ')[0].strip()
                                            name3 = line2.split(' ')[1].strip()
                                            valor13 = line2.split('=')[1].strip()
                                            valor3 = valor13.replace(';','')
                        
                                            var = var.var(type3,name3,valor3,"local",self.numlines(line2))
                                            self.table.Insert(name3,var)
                                
                                else:
                                    contenido = contenido + line2
                                    cont2 = cont2 + 1

                                    for i in range(len(self.tokens)):
                                        if line2.split(' ')[0].strip() == self.tokens[i]:
                                            type3 = line2.split(' ')[0].strip()
                                            name3 = line2.split(' ')[1].strip()
                                            valor13 = line2.split('=')[1].strip()
                                            valor3 = valor13.replace(';','')
                        
                                            var = Variable.Variable(type3,name3,valor3,"local",self.numlines(line2))
                                            self.table.Insert(name3,var)
                            
                         

                     funcion = Funcion.Funcion(line.split(' ')[0].strip(),name,contenido,self.numlines(line2))
                     self.table.Insert(name,funcion)

                else:
                    if(cont2 == 0):
                        if line.count(" ") == 2:
                             name = line.split(' ')[0].strip()
                             valor1 = line.split('=')[1].strip()
                             valor = valor1.replace(';','')

                             var = var.var(None,name,valor,"global",self.numlines(line))
                             self.table.Insert(name,var)
                        else:
                            type = line.split(' ')[0].strip()
                            name = line.split(' ')[1].strip()
                            valor1 = line.split('=')[1].strip()
                            valor = valor1.replace(';','')
                        
                            var = Variable.Variable(type,name,valor,"global",self.numlines(line))
                            self.table.Insert(name,var)
                    elif line.count(" ") == 3:
                        type = line.split(' ')[0].strip()
                        name = line.split(' ')[1].strip()
                        valor1 = line.split('=')[1].strip()
                        valor = valor1.replace(';','')

                        var = Variable.Variable(type,name,valor,"global",self.numlines(line))
                        self.table.Insert(name,var)
                    elif line.count(" ") == 2:
                        name = line.split(' ')[0].strip()
                        valor1 = line.split('=')[1].strip()
                        valor = valor1.replace(';','')

                        var = var.var(None,name,valor,"global",self.numlines(line))
                        self.table.Insert(name,var)

    

    def tieneParametros(self,line):
        x = re.search('\(' '\)',line)

        if(x):
            return False
        return True

   

    def types(self,type):#Tipos de variables a verificar
        if type == "int":
            return int
        if type == "string":
            return str
        if type == "float":
            return float

    def isInt(self,line):#Verifica si hay una variable INT en una linea de texto
        x = re.search('int',line)
        if(x):
            return True
        else:
            return False

    def numlines(self,searchLin):
        cont = 1
        with open("codigo.txt", "r") as f:
            for line in f:
                if line == searchLin:
                    return cont
                cont = cont +1

    def _while_if(self,line):#Verifica si es un While IF
        x = re.search('if',line)
        y = re.search('while',line)

        if x or y:
            return True
        return False

    def isFloat(self,var):#Verifica si una variable es FLOAT
        try:
             float(var)
             return True
        except:
             return False
          
    def es_int(self,var):#Verifica si una variable es INT
        try:
            int(var)
            return True
        except:
            return False

    def imprimir(self):#Imprime reglon de texto
            print(self.table.Search('cadena').getValor())


    def imprimirArchivo(self):#imprimi archivo de texto a evaluar
        cont = 1
        with open("codigo.txt", "r") as f:
            for line in f:
                print(cont , " ", line,end='')
                cont = cont+1
            print()

    def _estaenlatable(self,var):#Verifica si la variable esta en la Hash Table
        if self.table.Search(var) != None:
            return True
        return False

    def _errorDecontenidoFunciones(self):#Devuelve el Error y la linea en la que se encuentra
         cont = 0
         contu = 0
         cont = 0
         with open("codigo.txt", "r") as f:
            for line in f:
                cont = 0
                if self.isFuncion(line) is True and self._while_if(line) is False:
                    name = line.split(' ')[1].strip() 
                    contenido = self.table.Search(name).getCuerpo()                       
                    for i in contenido:
                        if i == '\n':
                            cont = cont + 1

                    for line2 in f:
                        if line2 !=' ':
                            type  = self.table.Search(name).getTipo()
                            x = re.search('return',contenido)

                            if(x and type == "void" and cont == 0):
                                print("Error en line:" , self.numlines(line2)  , " 'return' no valido en funciones void")
                                cont = cont+1
                        
                            if line2.split(' ')[0].strip() == "return":
                                nameV1 = line2.split(' ')[1].strip()
                                nameV  = nameV1.replace(';','')
                                if self._estaenlatable(nameV) == True:
                                    typeV = self.table.Search(nameV).getTipo()
                            
                                    if typeV == None:
                                        print("Error en line:" , self.numlines(line2) + cont ,"La var ", "'",self.table.Search(nameV).getname(),"'", " No esta declarada")

                                    elif typeV != type:
                                            print("Error en line:" , self.numlines(line2)  , " valor de retorno no coincide con el type de funcion")
                                else:
                                    if self.es_int(nameV) == False and self.isFloat(nameV) == False:
                                        if type != "string":
                                            print("Error en line:" , self.numlines(line2)  , " valor de retorno no coincide con el type de funcion")

                                    if self.es_int(nameV) == True or self.isFloat(nameV) == True:
                                        if type != "int" and "float":
                                            print("Error en line:" , self.numlines(line2)  , " valor de retorno no coincide con el type de funcion")

                            if line2.count(" ") == 2:
                                conta = 0
                                nameV2 = line2.split(' ')[0].strip()
                                valor12 = line2.split('=')[1].strip()
                                valor2 = valor12.replace(';','')

      
                                if self.es_int(valor2) == True and conta == 0:
                                        if self.table.Search(nameV2).gettype() != "int":
                                            print("Error en line:" , self.numlines(line2) , " valor del type de var","'",self.table.Search(nameV2).getname(),"'","no coincide")
                                            conta = conta+1
                                         
                                if self.isFloat(valor2) == True and self.table.Search(nameV2).getAlcance() == "local" and conta == 0:
                                    if self.table.Search(nameV2).gettype() != "float":
                                        print("Error en line:" , self.numlines(line2) , " valor del type de var","'",self.table.Search(nameV2).getname(),"'","no coincide")
                                        conta = conta + 1

                                if self.isFloat(valor2) == False and self.es_int(valor2) == False:
                                    if self.table.Search(nameV2).getTipo() != "string":
                                        print("Error en line:" , self.numlines(line2) , " valor del type de var","'",self.table.Search(nameV2).getNombre(),"'","no coincide")
                                conta = 0   

                            nameParametro = ""
                            if self._while_if(line2) is True:
                                    nameParametro = line2.split(' ')[2].strip() 
                                    if self.table.Search(nameParametro) == None:
                                        print("Error en line:" , self.numlines(line2) , " La var ","'", nameParametro,"'", " no esta declarada")
                            contu = contu + 1
                            if contu == cont:
                                break

    def _errorAsignacion(self):#Verifica la asignacion de int, void , string
        cont = 0
        cont2 = 0

        with open("codigo.txt", "r") as f:
            for line in f:
                if self.isFuncion(line) is True and self._while_if(line) is False:
                     name = line.split(' ')[1].strip() 
                     for i in range(len(self.tokens)):
                         if self.table.Search(name).getTipo() != self.tokens[i]:
                             cont = cont + 1
                     if cont == 4:  
                         print("Error en line:" , self.numlines(line) , " type de dato: " + self.table.Search(name).gettype() + " no valido")
                     cont = 0 
                else:
                    if line.count(" ") == 3:
                        name = line.split(' ')[1].strip()
                        for i in range(len(self.tokens)):
                                if self.table.Search(name).getTipo() != self.tokens[i]:
                                   cont = cont + 1
                        if cont == 4:  
                                 if self.table.Search(name).gettype() != None:
                                     print("Error en line:" , self.numlines(line) , " type de dato: " , self.table.Search(name).gettype() , " no valido")
                                 if self.table.Search(name).gettype() == None:
                                     print("Error en line:" , self.numlines(line) ,"La var " ,"'",self.table.Search(name).getname(),"'",self.table.Search(name).getname(), " No esta declarada")
                        cont = 0

                        if self.table.Search(name).getValor().isdigit() == True:
                             if self.types(self.table.Search(name).getTipo) != int and self.types(self.table.Search(name).getTipo()) != float:
                                   print("Error en line:" , self.numlines(line) , " valor del type de var",self.table.Search(name).getNombre(),"no coincide")

                        if self.table.Search(name).getValor().isdigit() != True and self.isFloat(self.table.Search(name).getValor()) is False:
                            if self._estaenlatable(self.table.Search(name).getValor()) == True:
                                if self.types(self.table.Search(name).getTipo()) != str and self.table.Search(self.table.Search(name).getValor()).getTipo() != self.table.Search(name).getTipo():
                                    print("Error en line:" , self.numlines(line) , " valor del type de var",self.table.Search(name).getNombre(),"no coincide")
                            else:
                                if self.types(self.table.Search(name).getTipo()) != str:
                                    print("Error en line:" , self.numlines(line) , " valor del type de var",self.table.Search(name).getname(),"no coincide")
                        if  self.isFloat(self.table.Search(name).getValor()) == True and self.table.Search(name).getValor().isdigit() == False:
                             if self.types(self.table.Search(name).gettype()) != float:
                                   print("Error en line:" , self.numlines(line) , " valor del type de var",self.table.Search(name).getname(),"no coincide")
                                
                        
                    elif line.count(" ") == 2:
                        name = line.split(' ')[0].strip()    
                        for i in range(len(self.tokens)):
                              if self.table.Search(name).getTipo() != self.tokens[i]:
                                  cont = cont + 1
                        if cont == 4:  
                                 if self.table.Search(name).gettype() != None:
                                     print("Error en line:" , self.numlines(line) , " type de dato: " , self.table.Search(name).gettype() , " no valido")
                                 if self.table.Search(name).gettype() == None:
                                     print("Error en line:" , self.numlines(line) ,"La var ", "'",self.table.Search(name).getname(),"'", " No esta declarada")
                        cont = 0

                        
                        



