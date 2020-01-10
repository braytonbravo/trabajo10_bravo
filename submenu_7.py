import libreria

def agregarOceano():
    opc=0
    max=3
    while ( opc != max ):
        print("######   VARIEDADES DE PECES   ######")
        print("#1.Agregar peces       #")
        print("#2.Mostrar peces       #")
        print("#3.salir                #")
        print("#########################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        agregarPeces()
    if (opc==2):
        mostrarPeces()


opc=0
max=3
while ( opc != max ):
    print("######   OCEANOS   ######")
    print("#1.Agregar Oceano       #")
    print("#2.Mostrar Oceano       #")
    print("#3.salir                #")
    print("#########################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        agregarOceano()
    if (opc==2):
        mostrarOceano()


