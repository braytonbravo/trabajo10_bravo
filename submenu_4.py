import libreria

def nombrePais():
    opc=0
    max=3
    while ( opc != max ):
        print("######  continente americano  ######")
        print("#1.SUR AMERICA     #")
        print("#2.NORTE AMERICA   #")
        print("#3.salir")
        print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        nombrePais()
    if (opc==2):
        agregarPais()

opc=0
max=3
while ( opc != max ):
    print("######  PAISES  ######")
    print("#1.Nobre del pais")
    print("#2.Agregar Pais")
    print("#3.salir")
    print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        nombrePais()
    if (opc==2):
        agregarPais()


