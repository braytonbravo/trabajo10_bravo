import libreria

def agregarSuyos():
    nombre=libreria.pedir_suyos("Ingrese nombre del suyo:")
    contenido=nombre+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("suyo agregado agregado")

def mostrarSuyos():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()

opc=0
max=3
while ( opc != max ):
    print("######   Los Suyos del Tahuntisuyo   ######")
    print("#1.Agregar Suyos")
    print("#2.Mostrar Suyos")
    print("#3.Salir             #")
    print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        agregarSuyos()
    if (opc==2):
        mostrarSuyos()


