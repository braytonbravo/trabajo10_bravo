import libreria
opc=0
max=3

def agregarAlumno():
    nombre=libreria.pedir_nombre("Ingrrese alumno:")
    nota=libreria.pedir_entero("Ingrese el costo:", 1,20)
    contenido=nombre+"-"+str(nota)+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Alumno agregado")

def mostrarAlumno():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()

while ( opc != max ):
    print("###### LISTA DE ALUMNOS   ######")
    print("#1.Agregar Alumno  ")
    print("#2.Mostrar Alumno  ")
    print("#3.salir")
    print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        agregarAlumno()
    if (opc==2):
        mostrarAlumno()


