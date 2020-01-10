import libreria

def agregarOceano():
    nombre=libreria.pedir_oceano("Ingrese oceano:")
    contenido=nombre+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Oceano agregado")

def mostrarOceano():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()

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

