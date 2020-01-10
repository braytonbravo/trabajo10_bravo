import libreria

def nuevoJugador():
    nombre=libreria.pedir_nombre("Ingrese nombre jugador:")
    camiseta=libreria.pedir_entero("Ingrese numero de camiseta:", 1,35)
    contenido=nombre+"_"+str(camiseta)+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Jugador nuevo guardado")



def mostrarJugadores():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()

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
