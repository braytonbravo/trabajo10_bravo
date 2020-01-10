import libreria


def agregarPosicion():
    nombre=libreria.pedir_nombre("Ingrese posicion de jugador:")
    contenido=nombre+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Posicion guardado")

def mostrarPosicion():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()


def nuevoJugador():
    opc=0
    max=3
    while ( opc != max ):
        print("#######    Posicion de jugador   #######")
        print("#1. Agregar Posicion         #")
        print("#2. Mostrar Posicion:     #")
        print("#3. Salir                  #")
        print("############################")

    opc=libreria.pedir_entero("Ingrese opcion:", 1,3)

    if ( opc == 1):
        agregarPosicion()

    if ( opc == 2):
        mostrarPosicion()



opc=0
max=3
while ( opc != max ):
    print("#######    LISTA DE JUGADORES    #######")
    print("#1. Nuevo jugador:         #")
    print("#2. Mostrar jugadores:     #")
    print("#3. Salir                  #")
    print("############################")

    opc=libreria.pedir_entero("Ingrese opcion:", 1,3)

    if ( opc == 1):
        nuevoJugador()

    if ( opc == 2):
        mostrarJugadores()

