import re
import TablaHash
import Funcion
import Variable


class AnalizadorSemantico:
    def __init__(self):
        self.tabla = TablaHash.TablaHash()
        self.tokens = ['void','int','float','string']
        

    def buscar(self,num):
        return self.tabla.searchTableHash(num)
        

    def _esFuncion(self,linea):
        y = re.search('\(',linea)
        if(y):  
            return True
        else:
            return False

    def crear_tabla(self):
        contador = 0
        cuerpo = ""
        booleana = bool(0)
        contador2 = 0

        with open("codigo.txt", "r") as f:
            for linea in f:
                if self._esFuncion(linea) is True:
                     nombre = linea.split(' ')[1].strip() 
                     contador = contador + 1
                     cuerpo = ""
                     for linea2 in f:
                         if linea2 != ' ':
                            x = re.search('\{',linea2)
                            y = re.search('\}',linea2)
                            if(x):
                                z = re.search(nombre,linea2)
                                if (z):
                                    contador = contador + 1
                                    contador2 = contador2 + 1
                                else:
                                    if(self._tieneParametros(linea) == True):
                                        x1 = 3
                                        while x1 < linea.count(" ") - 1:
                                            if  linea.split(' ')[x1].strip() != ',':
                                                tipoV = linea.split(' ')[x1].strip()
                                            if  linea.split(' ')[x1+1].strip() != ',':
                                                nombreV = linea.split(' ')[x1+1].strip()
                                            variable = Variable.Variable(tipoV,nombreV,None,"local",self._numerodelineas(linea2))
                                            self.tabla.insertTableHash(nombreV,variable)
                                            x1 = x1 + 3
                                 
                                    cuerpo = cuerpo + linea2
                                    contador = contador+1
                                    contador2 = contador2 + 1
                                 
                                    for i in range(len(self.tokens)):
                                        if linea2.split(' ')[0].strip() == self.tokens[i]:
                                            tipo3 = linea2.split(' ')[0].strip()
                                            nombre3 = linea2.split(' ')[1].strip()
                                            if tipo3 == "int":
                                                valor13 = linea2.split('=')[1].strip()
                                                valor3 = valor13.replace(';','')
                                            
                                            variable = Variable.Variable(tipo3,nombre3,valor3,"local",self._numerodelineas(linea2))
                                            self.tabla.insertTableHash(nombre3,variable)
                            else:
                                if(y):
                                    contador = contador-1
                                    if(contador == 0): 
                                        break
                                    cuerpo = cuerpo + linea2
                                    contador2 = contador2 + 1

                                    for i in range(len(self.tokens)):
                                        if linea2.split(' ')[0].strip() == self.tokens[i]:
                                            tipo3 = linea2.split(' ')[0].strip()
                                            nombre3 = linea2.split(' ')[1].strip()
                                            valor13 = linea2.split('=')[1].strip()
                                            valor3 = valor13.replace(';','')
                        
                                            variable = Variable.Variable(tipo3,nombre3,valor3,"local",self._numerodelineas(linea2))
                                            self.tabla.insertTableHash(nombre3,variable)
                                
                                else:
                                    cuerpo = cuerpo + linea2
                                    contador2 = contador2 + 1

                                    for i in range(len(self.tokens)):
                                        if linea2.split(' ')[0].strip() == self.tokens[i]:
                                            tipo3 = linea2.split(' ')[0].strip()
                                            nombre3 = linea2.split(' ')[1].strip()
                                            valor13 = linea2.split('=')[1].strip()
                                            valor3 = valor13.replace(';','')
                        
                                            variable = Variable.Variable(tipo3,nombre3,valor3,"local",self._numerodelineas(linea2))
                                            self.tabla.insertTableHash(nombre3,variable)
                            
                         

                     funcion = Funcion.Funcion(linea.split(' ')[0].strip(),nombre,cuerpo,self._numerodelineas(linea2))
                     self.tabla.insertTableHash(nombre,funcion)

                else:
                    if(contador2 == 0):
                        if linea.count(" ") == 2:
                             nombre = linea.split(' ')[0].strip()
                             valor1 = linea.split('=')[1].strip()
                             valor = valor1.replace(';','')

                             variable = Variable.Variable(None,nombre,valor,"global",self._numerodelineas(linea))
                             self.tabla.insertTableHash(nombre,variable)
                        else:
                            tipo = linea.split(' ')[0].strip()
                            nombre = linea.split(' ')[1].strip()
                            valor1 = linea.split('=')[1].strip()
                            valor = valor1.replace(';','')
                        
                            variable = Variable.Variable(tipo,nombre,valor,"global",self._numerodelineas(linea))
                            self.tabla.insertTableHash(nombre,variable)
                    elif linea.count(" ") == 3:
                        tipo = linea.split(' ')[0].strip()
                        nombre = linea.split(' ')[1].strip()
                        valor1 = linea.split('=')[1].strip()
                        valor = valor1.replace(';','')

                        variable = Variable.Variable(tipo,nombre,valor,"global",self._numerodelineas(linea))
                        self.tabla.insertTableHash(nombre,variable)
                    elif linea.count(" ") == 2:
                        nombre = linea.split(' ')[0].strip()
                        valor1 = linea.split('=')[1].strip()
                        valor = valor1.replace(';','')

                        variable = Variable.Variable(None,nombre,valor,"global",self._numerodelineas(linea))
                        self.tabla.insertTableHash(nombre,variable)

    def _imprimir(self):
        print(self.tabla.searchTableHash('cadena').getValueVar())

    def _tieneParametros(self,linea):
        x = re.search('\(' '\)',linea)

        if(x):
            return False
        return True

    def _esInt(self,linea):
        x = re.search('int',linea)
        if(x):
            return True
        else:
            return False

    def _cualTipoes(self,tipo):
        if tipo == "int":
            return int
        if tipo == "string":
            return str
        if tipo == "float":
            return float

    def _numerodelineas(self,lineaAbuscar):
        contador = 1
        with open("codigo.txt", "r") as f:
            for linea in f:
                if linea == lineaAbuscar:
                    return contador
                contador = contador +1

    def _while_if(self,linea):
        x = re.search('if',linea)
        y = re.search('while',linea)

        if x or y:
            return True
        return False

    def es_flotante(self,variable):
        try:
             float(variable)
             return True
        except:
             return False
          
    def es_int(self,variable):
        try:
            int(variable)
            return True
        except:
            return False


    def _imprimirArchivo(self):
        contador = 1
        with open("codigo.txt", "r") as f:
            for linea in f:
                print(contador , " ", linea,end='')
                contador = contador+1
            print()

    def _estaenlaTabla(self,variable):
        if self.tabla.searchTableHash(variable) != None:
            return True
        return False

    def _errorDeCuerpoFunciones(self):
         contador = 0
         contu = 0
         cont = 0
         with open("codigo.txt", "r") as f:
            for linea in f:
                cont = 0
                if self._esFuncion(linea) is True and self._while_if(linea) is False:
                    nombre = linea.split(' ')[1].strip() 
                    cuerpo = self.tabla.searchTableHash(nombre).getContenidoFuncion()
                    
                    for i in cuerpo:
                        if i == '\n':
                            contador = contador + 1

                    for linea2 in f:
                        if linea2 !=' ':
                            tipo  = self.tabla.searchTableHash(nombre).getTypeFuncion()
                            x = re.search('return',cuerpo)

                            if(x and tipo == "void" and cont == 0):
                                print("Error en linea:" , self._numerodelineas(linea2)  , " 'return' no valido en funciones void")
                                cont = cont+1
                        
                            if linea2.split(' ')[0].strip() == "return":
                                nombreV1 = linea2.split(' ')[1].strip()
                                nombreV  = nombreV1.replace(';','')
                                if self._estaenlaTabla(nombreV) == True:
                                    tipoV = self.tabla.searchTableHash(nombreV).getTypeVar()
                            
                                    if tipoV == None:
                                        print("Error en linea:" , self._numerodelineas(linea2) + contador ,"La variable ", "'",self.tabla.searchTableHash(nombreV).getNameVar(),"'", " No esta declarada")

                                    elif tipoV != tipo:
                                            print("Error en linea:" , self._numerodelineas(linea2)  , " valor de retorno no coincide con el tipo de funcion")
                                else:
                                    if self.es_int(nombreV) == False and self.es_flotante(nombreV) == False:
                                        if tipo != "string":
                                            print("Error en linea:" , self._numerodelineas(linea2)  , " valor de retorno no coincide con el tipo de funcion")

                                    if self.es_int(nombreV) == True or self.es_flotante(nombreV) == True:
                                        if tipo != "int" and "float":
                                            print("Error en linea:" , self._numerodelineas(linea2)  , " valor de retorno no coincide con el tipo de funcion")

                            if linea2.count(" ") == 2:
                                conta = 0
                                nombreV2 = linea2.split(' ')[0].strip()
                                valor12 = linea2.split('=')[1].strip()
                                valor2 = valor12.replace(';','')

      
                                if self.es_int(valor2) == True and conta == 0:
                                        if self.tabla.searchTableHash(nombreV2).getTypeVar() != "int":
                                            print("Error en linea:" , self._numerodelineas(linea2) , " valor del tipo de variable","'",self.tabla.searchTableHash(nombreV2).getNameVar(),"'","no coincide")
                                            conta = conta+1
                                         
                                if self.es_flotante(valor2) == True and self.tabla.searchTableHash(nombreV2).getAlcanceVar() == "local" and conta == 0:
                                    if self.tabla.searchTableHash(nombreV2).getTypeVar() != "float":
                                        print("Error en linea:" , self._numerodelineas(linea2) , " valor del tipo de variable","'",self.tabla.searchTableHash(nombreV2).getNameVar(),"'","no coincide")
                                        conta = conta + 1

                                if self.es_flotante(valor2) == False and self.es_int(valor2) == False:
                                    if self.tabla.searchTableHash(nombreV2).getTypeVar() != "string":
                                        print("Error en linea:" , self._numerodelineas(linea2) , " valor del tipo de variable","'",self.tabla.searchTableHash(nombreV2).getNameVar(),"'","no coincide")
                                conta = 0   

                            nombreParametro = ""
                            if self._while_if(linea2) is True:
                                    nombreParametro = linea2.split(' ')[2].strip() 
                                    if self.tabla.searchTableHash(nombreParametro) == None:
                                        print("Error en linea:" , self._numerodelineas(linea2) , " La variable ","'", nombreParametro,"'", " no esta declarada")
                            contu = contu + 1
                            if contu == contador:
                                break

    def _errorAsignacion(self):
        contador = 0
        contador2 = 0

        with open("codigo.txt", "r") as f:
            for linea in f:
                if self._esFuncion(linea) is True and self._while_if(linea) is False:
                     nombre = linea.split(' ')[1].strip() 
                     for i in range(len(self.tokens)):
                         if self.tabla.searchTableHash(nombre).getTypeFuncion() != self.tokens[i]:
                             contador = contador + 1
                     if contador == 4:  
                         print("Error en linea:" , self._numerodelineas(linea) , " Tipo de dato: " + self.tabla.searchTableHash(nombre).getTypeVar() + " no valido")
                     contador = 0 
                else:
                    if linea.count(" ") == 3:
                        nombre = linea.split(' ')[1].strip()
                        for i in range(len(self.tokens)):
                                if self.tabla.searchTableHash(nombre).getTypeVar() != self.tokens[i]:
                                   contador = contador + 1
                        if contador == 4:  
                                 if self.tabla.searchTableHash(nombre).getTypeVar() != None:
                                     print("Error en linea:" , self._numerodelineas(linea) , " Tipo de dato: " , self.tabla.searchTableHash(nombre).getTypeVar() , " no valido")
                                 if self.tabla.searchTableHash(nombre).getTypeVar() == None:
                                     print("Error en linea:" , self._numerodelineas(linea) ,"La variable " ,"'",self.tabla.searchTableHash(nombre).getNameVar(),"'",self.tabla.searchTableHash(nombre).getNameVar(), " No esta declarada")
                        contador = 0

                        if self.tabla.searchTableHash(nombre).getValueVar().isdigit() == True:
                             if self._cualTipoes(self.tabla.searchTableHash(nombre).getTypeVar()) != int and self._cualTipoes(self.tabla.searchTableHash(nombre).getTypeVar()) != float:
                                   print("Error en linea:" , self._numerodelineas(linea) , " valor del tipo de variable",self.tabla.searchTableHash(nombre).getNameVar(),"no coincide")

                        if self.tabla.searchTableHash(nombre).getValueVar().isdigit() != True and self.es_flotante(self.tabla.searchTableHash(nombre).getValueVar()) is False:
                            if self._estaenlaTabla(self.tabla.searchTableHash(nombre).getValueVar()) == True:
                                if self._cualTipoes(self.tabla.searchTableHash(nombre).getTypeVar()) != str and self.tabla.searchTableHash(self.tabla.searchTableHash(nombre).getValueVar()).getTypeVar() != self.tabla.searchTableHash(nombre).getTypeVar():
                                    print("Error en linea:" , self._numerodelineas(linea) , " valor del tipo de variable",self.tabla.searchTableHash(nombre).getNameVar(),"no coincide")
                            else:
                                if self._cualTipoes(self.tabla.searchTableHash(nombre).getTypeVar()) != str:
                                    print("Error en linea:" , self._numerodelineas(linea) , " valor del tipo de variable",self.tabla.searchTableHash(nombre).getNameVar(),"no coincide")
                        if  self.es_flotante(self.tabla.searchTableHash(nombre).getValueVar()) == True and self.tabla.searchTableHash(nombre).getValueVar().isdigit() == False:
                             if self._cualTipoes(self.tabla.searchTableHash(nombre).getTypeVar()) != float:
                                   print("Error en linea:" , self._numerodelineas(linea) , " valor del tipo de variable",self.tabla.searchTableHash(nombre).getNameVar(),"no coincide")
                                
                        
                    elif linea.count(" ") == 2:
                        nombre = linea.split(' ')[0].strip()    
                        for i in range(len(self.tokens)):
                              if self.tabla.searchTableHash(nombre).getTypeVar() != self.tokens[i]:
                                  contador = contador + 1
                        if contador == 4:  
                                 if self.tabla.searchTableHash(nombre).getTypeVar() != None:
                                     print("Error en linea:" , self._numerodelineas(linea) , " Tipo de dato: " , self.tabla.searchTableHash(nombre).getTypeVar() , " no valido")
                                 if self.tabla.searchTableHash(nombre).getTypeVar() == None:
                                     print("Error en linea:" , self._numerodelineas(linea) ,"La variable ", "'",self.tabla.searchTableHash(nombre).getNameVar(),"'", " No esta declarada")
                        contador = 0

                        
                        



