import libreria
opc=0
max=3

def agregarVocales():
    nombre=libreria.pedir_vocales("Ingrese vocal:")
    contenido=nombre+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("vocal agregado")

def mostrarVocales():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()

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


