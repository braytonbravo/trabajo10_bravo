import libreria

def nombreMes():
    opc=0
    max=3
    while ( opc != max ):
        print("######  AÑO   ######")
        print("#1.Nombre del año            #")
        print("#2.Mostrar nombre del año    #")
        print("#3.salir                     #")
        print("##############################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        nombreAño()
    if (opc==2):
        mostrarNombre()

def nombreNombre():
    nombre=libreria.pedir_nombre("Ingrese nombre:")
    contenido=nombre+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Nombre del año guardado")

def agregarDatos():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()


opc=0
max=3
while ( opc != max ):
    print("######  MESES DEL AÑO   ######")
    print("#1.Nombre del mes:           #")
    print("#2.Mostrar mes y dia         #")
    print("#3.salir                     #")
    print("##############################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        nombreMes()
    if (opc==2):
        mostrarMesdia()


