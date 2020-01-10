import libreria

def nombrePais():
    nombre=libreria.pedir_nombre("Ingrese Pais:")
    contenido=nombre+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Pais agregado")
def agregarPais():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()
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
