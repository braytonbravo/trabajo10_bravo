import libreria


def agregarSuyos():
    opc=0
    max=3
    while ( opc != max ):
        print("######   Incas   ######")
        print("#1.Nombre Incas")
        print("#2.Mostrar Incas")
        print("#3.Salir             #")
        print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        agregarInca()
    if (opc==2):
        mostrarInca()




opc=0
max=3
while ( opc != max ):
    print("######   Los Suyos del Tahuntisuyo   ######")
    print("#1.Agregar Suyos")
    print("#2.Mostrar Suyos")
    print("#3.Salir             #")
    print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        agregarSuyos()
    if (opc==2):
        mostrarSuyos()

