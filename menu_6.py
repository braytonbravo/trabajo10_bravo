import libreria

def agregarMaravilla():
    nombre=libreria.pedir_maravilla("Ingrese Maravilla:")
    contenido=nombre+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Maravilla del mundo agregado")

def mostrarMaravilla():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()



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

