import AnalizadorSemantico

analizador = AnalizadorSemantico.AnalizadorSemantico()

analizador._imprimirArchivo()
print()
analizador.crear_tabla()
analizador._errorAsignacion()
analizador._errorDeCuerpoFunciones()
print()


