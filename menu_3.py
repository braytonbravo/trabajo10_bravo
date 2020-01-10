import libreria

def almuerzos():
    nombre=libreria.pedir_nombre("Ingrrese almuerzo:")
    costo=libreria.pedir_entero("Ingrese el costo:", 1,15)
    contenido=nombre+"-"+str(costo)+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Aluerzon conprado")
def mostrarAlmuerzo():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()
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


