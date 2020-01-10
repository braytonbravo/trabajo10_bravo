import libreria

def nombreMes():
    nombre=libreria.pedir_nombre("Ingrese mes:")
    dia=libreria.pedir_entero("Ingrese dia:", 1,31)
    contenido=nombre+"-"+str(dia)+"\n"
    libreria.agregar_datos("info.text",contenido,"a")
    print("Mes y Dia guardado")

def mostrarMesdia():
    archivo=open("info.text")
    datos=archivo.read()
    print(datos)
    archivo.close()

opc=0
max=3
while ( opc != max ):
    print("######  MESES DEL AÑO   ######")
    print("#1.Nombre del mes:           #")
    print("#2.Mostrar mes y dia         #")
    print("#3.salir                     #")
    print("##############################")

    opc=libreria.pedir_entero("Ingres opcion:", 1,3)

    if (opc==1):
        nombreMes()
    if (opc==2):
        mostrarMesdia()

