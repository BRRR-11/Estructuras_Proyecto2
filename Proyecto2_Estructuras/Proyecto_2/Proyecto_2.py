import AnalizadorSemantico

analizador = AnalizadorSemantico.AnalizadorSemantico()

analizador.imprimirArchivo()
print()
analizador.createTable()
analizador._errorAsignacion()
analizador._errorDecontenidoFunciones()
print()


