import libreria


def agregarVocales():
    opc=0
    max=3
    while ( opc != max ):
         print("###### ABECEDARIO    ######")
         print("#1.Agrega ABECEDARIO #")
         print("#2.Mostrar ABECEDARIO #")
         print("#3.salir             #")
         print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        agregarAbecedario()
    if (opc==2):
        mostrarAbecedario()


opc=0
max=3

while ( opc != max ):
    print("###### LAS VOCALES    ######")
    print("#1.Agregar Vocales")
    print("#2.Mostrar Vocales")
    print("#3.salir             #")
    print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        agregarVocales()
    if (opc==2):
        mostrarVocales()



