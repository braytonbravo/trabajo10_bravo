import libreria

def datos():
    nombre=libreria.pedir_nombre("Ingrese nombre:")
    sexo=libreria.pedir_sexo("Ingrese sexo:")
    edad=libreria.pedir_entero("Ingrese edad:", 1,100)
    contenido=nombre+"-"+sexo+"-"+str(edad)+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Datos guardados")

def agregarDatos():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()


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

