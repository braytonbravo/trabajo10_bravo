import libreria

def mesero():
    nombre=libreria.pedir_nombre("Ingrrese mesero:")
    contenido=nombre+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Mesero  conprado")
def mostrarAlmuerzo():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()

def agregarAlmuerzo():
    opc=0
    max=3
    while ( opc != max ):
        print("######  Mesero  ######")
        print("#1.Nombre Mesero      #")
        print("#2.Agregar Mesero  #")
        print("#3.SALIR              #")
        print("#######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        mesero()
    if (opc==2):
        mostrarMesero


opc=0
max=3
while ( opc != max ):
    print("######  MENU  ######")
    print("#1.ALMUERZOS          #")
    print("#2.MOSTRAR ALMUERZOS  #")
    print("#3.SALIR              #")
    print("#######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        almuerzos()
    if (opc==2):
        mostrarAlmuerzo

