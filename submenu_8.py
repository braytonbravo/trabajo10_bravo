import libreria

def agregarAlumno():
    opc=0
    max=3
    while ( opc != max ):
        print("###### Institucion Educativa   ######")
        print("#1.Agregar COLEGIO  ")
        print("#2.Mostrar COLEGIO ")
        print("#3.salir")
        print("######################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        colegio()
    if (opc==2):
        mostrarColegio()


opc=0
max=3
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

