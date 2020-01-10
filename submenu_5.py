import libreria

def datos():
    opc=0
    max=3
    while ( opc != max ):
        print("######  Datos ######")
        print("#1.Nombres             #")
        print("#2.Sexo                #")
        print("#4.salir")
        print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        nombres()
    if (opc==2):
        agregarSexo()

opc=0
max=3
while ( opc != max ):
    print("######  DOCUMENTO NACIONAL DE IDENTIDAD ######")
    print("#1.Datos             #")
    print("#2.Agregar Datos     #")
    print("#4.salir")
    print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        datos()
    if (opc==2):
        agregarDatos()

