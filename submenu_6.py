import libreria

def agregarMaravilla():
    opc=0
    max=3
    while ( opc != max ):
        print("######  MACHUPICHU ######")
        print("#1.Lugar de origen  #")
        print("#2.Mostrar Lugar #")
        print("#3.salir")
        print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        lugar()
    if (opc==2):
        mostrarLugar()


opc=0
max=3
while ( opc != max ):
    print("######  Maravillas del Mundo ######")
    print("#1.Agregar Maravila  #")
    print("#2.Mostrar Maravilla #")
    print("#3.salir")
    print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        agregarMaravilla()
    if (opc==2):
        mostrarMaravilla()


