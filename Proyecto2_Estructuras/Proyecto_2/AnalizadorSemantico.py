import re
import TablaHash
import Funcion
import Variable


class AnalizadorSemantico:
    def __init__(self):
        self.tableHash = TablaHash.TablaHash()
        self.tokens = ['void','int','float','string']
        

    def search(self,num):
        return self.tableHash.searchTableHash(num)
        

    def isFuncion(self,linea):
        y = re.search('\(',linea)
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
                                                tipoV = line.split(' ')[x1].strip()
                                            if  line.split(' ')[x1+1].strip() != ',':
                                                nombreV = line.split(' ')[x1+1].strip()
                                            variable = Variable.Variable(tipoV,nombreV,None,"local",self.numLine(line2))
                                            self.tableHash.insertTableHash(nombreV,variable)
                                            x1 = x1 + 3
                                 
                                    contenido = contenido + line2
                                    cont = cont+1
                                    cont2 = cont2 + 1
                                 
                                    for i in range(len(self.tokens)):
                                        if line2.split(' ')[0].strip() == self.tokens[i]:
                                            tipo3 = line2.split(' ')[0].strip()
                                            nombre3 = line2.split(' ')[1].strip()
                                            if tipo3 == "int":
                                                valor13 = line2.split('=')[1].strip()
                                                valor3 = valor13.replace(';','')
                                            
                                            variable = Variable.Variable(tipo3,nombre3,valor3,"local",self.numLine(line2))
                                            self.tableHash.insertTableHash(nombre3,variable)
                            else:
                                if(y):
                                    cont = cont-1
                                    if(cont == 0): 
                                        break
                                    contenido = contenido + line2
                                    cont2 = cont2 + 1

                                    for i in range(len(self.tokens)):
                                        if line2.split(' ')[0].strip() == self.tokens[i]:
                                            tipo3 = line2.split(' ')[0].strip()
                                            nombre3 = line2.split(' ')[1].strip()
                                            valor13 = line2.split('=')[1].strip()
                                            valor3 = valor13.replace(';','')
                        
                                            variable = Variable.Variable(tipo3,nombre3,valor3,"local",self.numLine(line2))
                                            self.tableHash.insertTableHash(nombre3,variable)
                                
                                else:
                                    contenido = contenido + line2
                                    cont2 = cont2 + 1

                                    for i in range(len(self.tokens)):
                                        if line2.split(' ')[0].strip() == self.tokens[i]:
                                            tipo3 = line2.split(' ')[0].strip()
                                            nombre3 = line2.split(' ')[1].strip()
                                            valor13 = line2.split('=')[1].strip()
                                            valor3 = valor13.replace(';','')
                        
                                            variable = Variable.Variable(tipo3,nombre3,valor3,"local",self.numLine(line2))
                                            self.tableHash.insertTableHash(nombre3,variable)
                            
                         

                     funcion = Funcion.Funcion(line.split(' ')[0].strip(),name,contenido,self.numLine(line2))
                     self.tableHash.insertTableHash(name,funcion)

                else:
                    if(cont2 == 0):
                        if line.count(" ") == 2:
                             name = line.split(' ')[0].strip()
                             valor1 = line.split('=')[1].strip()
                             valor = valor1.replace(';','')

                             variable = Variable.Variable(None,name,valor,"global",self.numLine(line))
                             self.tableHash.insertTableHash(name,variable)
                        else:
                            tipo = line.split(' ')[0].strip()
                            name = line.split(' ')[1].strip()
                            valor1 = line.split('=')[1].strip()
                            valor = valor1.replace(';','')
                        
                            variable = Variable.Variable(tipo,name,valor,"global",self.numLine(line))
                            self.tableHash.insertTableHash(name,variable)
                    elif line.count(" ") == 3:
                        tipo = line.split(' ')[0].strip()
                        name = line.split(' ')[1].strip()
                        valor1 = line.split('=')[1].strip()
                        valor = valor1.replace(';','')

                        variable = Variable.Variable(tipo,name,valor,"global",self.numLine(line))
                        self.tableHash.insertTableHash(name,variable)
                    elif line.count(" ") == 2:
                        nombre = line.split(' ')[0].strip()
                        valor1 = line.split('=')[1].strip()
                        valor = valor1.replace(';','')

                        variable = Variable.Variable(None,name,valor,"global",self.numLine(line))
                        self.tableHash.insertTableHash(name,variable)

    def mostrar(self):
        print(self.tableHash.searchTableHash('cadena').getValueVar())

    def tieneParametros(self,linea):
        x = re.search('\(' '\)',linea)

        if(x):
            return False
        return True

    def isInt(self,linea):
        x = re.search('int',linea)
        if(x):
            return True
        else:
            return False

    def whatType(self,typeT):
        if typeT == "int":
            return int
        if typeT == "string":
            return str
        if typeT == "float":
            return float

    def numLine(self,lineaAbuscar):
        contador = 1
        with open("codigo.txt", "r") as f:
            for linea in f:
                if linea == lineaAbuscar:
                    return contador
                contador = contador +1

    def whileAndIf(self,linea):
        x = re.search('if',linea)
        y = re.search('while',linea)

        if x or y:
            return True
        return False

    def isFlotante(self,variable):
        try:
             float(variable)
             return True
        except:
             return False
          
    def isIntV(self,variable):
        try:
            int(variable)
            return True
        except:
            return False


    def mostrarArchivo(self):
        contador = 1
        with open("codigo.txt", "r") as f:
            for line in f:
                print(contador , " ", line,end='')
                contador = contador+1
            print()

    def isInTable(self,variable):
        if self.tableHash.searchTableHash(variable) != None:
            return True
        return False

    def errorContenidoFunc(self):
         contador = 0
         contu = 0
         cont = 0
         with open("codigo.txt", "r") as f:
            for linea in f:
                cont = 0
                if self.isFuncion(linea) is True and self.whileAndIf(linea) is False:
                    nombre = linea.split(' ')[1].strip() 
                    cuerpo = self.tableHash.searchTableHash(nombre).getContenidoFuncion()
                    
                    for i in cuerpo:
                        if i == '\n':
                            contador = contador + 1

                    for linea2 in f:
                        if linea2 !=' ':
                            tipo  = self.tableHash.searchTableHash(nombre).getTypeFuncion()
                            x = re.search('return',cuerpo)

                            if(x and tipo == "void" and cont == 0):
                                print("Error en linea:" , self.numLine(linea2)  , " 'return' no valido en funciones void")
                                cont = cont+1
                        
                            if linea2.split(' ')[0].strip() == "return":
                                nombreV1 = linea2.split(' ')[1].strip()
                                nombreV  = nombreV1.replace(';','')
                                if self.isInTable(nombreV) == True:
                                    tipoV = self.tableHash.searchTableHash(nombreV).getTypeVar()
                            
                                    if tipoV == None:
                                        print("Error en linea:" , self.numLine(linea2) + contador ,"La variable ", "'",self.tableHash.searchTableHash(nombreV).getNameVar(),"'", " No esta declarada")

                                    elif tipoV != tipo:
                                            print("Error en linea:" , self.numLine(linea2)  , " valor de retorno no coincide con el tipo de funcion")
                                else:
                                    if self.isIntV(nombreV) == False and self.isFlotante(nombreV) == False:
                                        if tipo != "string":
                                            print("Error en linea:" , self.numLine(linea2)  , " valor de retorno no coincide con el tipo de funcion")

                                    if self.isIntV(nombreV) == True or self.isFlotante(nombreV) == True:
                                        if tipo != "int" and "float":
                                            print("Error en linea:" , self.numLine(linea2)  , " valor de retorno no coincide con el tipo de funcion")

                            if linea2.count(" ") == 2:
                                conta = 0
                                nombreV2 = linea2.split(' ')[0].strip()
                                valor12 = linea2.split('=')[1].strip()
                                valor2 = valor12.replace(';','')

      
                                if self.isIntV(valor2) == True and conta == 0:
                                        if self.tableHash.searchTableHash(nombreV2).getTypeVar() != "int":
                                            print("Error en linea:" , self.numLine(linea2) , " valor del tipo de variable","'",self.tableHash.searchTableHash(nombreV2).getNameVar(),"'","no coincide")
                                            conta = conta+1
                                         
                                if self.isFlotante(valor2) == True and self.tableHash.searchTableHash(nombreV2).getAlcanceVar() == "local" and conta == 0:
                                    if self.tableHash.searchTableHash(nombreV2).getTypeVar() != "float":
                                        print("Error en linea:" , self.numLine(linea2) , " valor del tipo de variable","'",self.tableHash.searchTableHash(nombreV2).getNameVar(),"'","no coincide")
                                        conta = conta + 1

                                if self.isFlotante(valor2) == False and self.isIntV(valor2) == False:
                                    if self.tableHash.searchTableHash(nombreV2).getTypeVar() != "string":
                                        print("Error en linea:" , self.numLine(linea2) , " valor del tipo de variable","'",self.tableHash.searchTableHash(nombreV2).getNameVar(),"'","no coincide")
                                conta = 0   

                            nombreParametro = ""
                            if self.whileAndIf(linea2) is True:
                                    nombreParametro = linea2.split(' ')[2].strip() 
                                    if self.tableHash.searchTableHash(nombreParametro) == None:
                                        print("Error en linea:" , self.numLine(linea2) , " La variable ","'", nombreParametro,"'", " no esta declarada")
                            contu = contu + 1
                            if contu == contador:
                                break

    def errorDeAsignacion(self):
        cont = 0
        #contador2 = 0

        with open("codigo.txt", "r") as f:
            for linea in f:
                if self.isFuncion(linea) is True and self.whileAndIf(linea) is False:
                     nombre = linea.split(' ')[1].strip() 
                     for i in range(len(self.tokens)):
                         if self.tableHash.searchTableHash(nombre).getTypeFuncion() != self.tokens[i]:
                             cont = cont + 1
                     if cont == 4:  
                         print("Error en linea:" , self.numLine(linea) , " Tipo de dato: " + self.tableHash.searchTableHash(nombre).getTypeVar() + " no valido")
                     cont = 0 
                else:
                    if linea.count(" ") == 3:
                        nombre = linea.split(' ')[1].strip()
                        for i in range(len(self.tokens)):
                                if self.tableHash.searchTableHash(nombre).getTypeVar() != self.tokens[i]:
                                   cont = cont + 1
                        if cont == 4:  
                                 if self.tableHash.searchTableHash(nombre).getTypeVar() != None:
                                     print("Error en linea:" , self.numLine(linea) , " Tipo de dato: " , self.tableHash.searchTableHash(nombre).getTypeVar() , " no valido")
                                 if self.tableHash.searchTableHash(nombre).getTypeVar() == None:
                                     print("Error en linea:" , self.numLine(linea) ,"La variable " ,"'",self.tableHash.searchTableHash(nombre).getNameVar(),"'",self.tableHash.searchTableHash(nombre).getNameVar(), " No esta declarada")
                        cont = 0

                        if self.tableHash.searchTableHash(nombre).getValueVar().isdigit() == True:
                             if self.whatType(self.tableHash.searchTableHash(nombre).getTypeVar()) != int and self.whatType(self.tableHash.searchTableHash(nombre).getTypeVar()) != float:
                                   print("Error en linea:" , self.numLine(linea) , " valor del tipo de variable",self.tableHash.searchTableHash(nombre).getNameVar(),"no coincide")

                        if self.tableHash.searchTableHash(nombre).getValueVar().isdigit() != True and self.isFlotante(self.tableHash.searchTableHash(nombre).getValueVar()) is False:
                            if self.isInTable(self.tableHash.searchTableHash(nombre).getValueVar()) == True:
                                if self.whatType(self.tableHash.searchTableHash(nombre).getTypeVar()) != str and self.tableHash.searchTableHash(self.tableHash.searchTableHash(nombre).getValueVar()).getTypeVar() != self.tableHash.searchTableHash(nombre).getTypeVar():
                                    print("Error en linea:" , self.numLine(linea) , " valor del tipo de variable",self.tableHash.searchTableHash(nombre).getNameVar(),"no coincide")
                            else:
                                if self.whatType(self.tableHash.searchTableHash(nombre).getTypeVar()) != str:
                                    print("Error en linea:" , self.numLine(linea) , " valor del tipo de variable",self.tableHash.searchTableHash(nombre).getNameVar(),"no coincide")
                        if  self.isFlotante(self.tableHash.searchTableHash(nombre).getValueVar()) == True and self.tableHash.searchTableHash(nombre).getValueVar().isdigit() == False:
                             if self.whatType(self.tableHash.searchTableHash(nombre).getTypeVar()) != float:
                                   print("Error en linea:" , self.numLine(linea) , " valor del tipo de variable",self.tableHash.searchTableHash(nombre).getNameVar(),"no coincide")
                                
                        
                    elif linea.count(" ") == 2:
                        nombre = linea.split(' ')[0].strip()    
                        for i in range(len(self.tokens)):
                              if self.tableHash.searchTableHash(nombre).getTypeVar() != self.tokens[i]:
                                  cont = cont + 1
                        if cont == 4:  
                                 if self.tableHash.searchTableHash(nombre).getTypeVar() != None:
                                     print("Error en linea:" , self.numLine(linea) , " Tipo de dato: " , self.tableHash.searchTableHash(nombre).getTypeVar() , " no valido")
                                 if self.tableHash.searchTableHash(nombre).getTypeVar() == None:
                                     print("Error en linea:" , self.numLine(linea) ,"La variable ", "'",self.tableHash.searchTableHash(nombre).getNameVar(),"'", " No esta declarada")
                        cont = 0

                        
                        



