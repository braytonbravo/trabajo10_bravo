def validar_entero_positivo(num):
    # 1. La instancia de num es int
    # 2. num > 0
    if (isinstance(num,int)):
        if (num > 0):
            return True
        else:
            return False
    else:
        return False
# fin_def

def validar_rango(num,ri,rf):
    # 1. Es un entero positivo
    # 2. Esta dentro del rango
    if (validar_entero_positivo(num) == True):
        if (num >= ri and num <= rf):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_entero(msg,ri,rf):
    n=0
    while(validar_entero_positivo(n)==False):
        n=input(msg)
        if (n.isdigit()== True):
            n=int(n)
    # fin_while
    return int(n)
#fin_def

######################################################3
# Libreria del menu de comandos
def pedir_entero_positivo(num):
    n=0
    while(validar_entero_positivo(n)==False):
        n=input(num)
        if (n.isdigit()):
            n=int(n)
    #fin while
    return int(n)

###########################################################
# Archivos
def validar_nombre(nombre):
    if (isinstance(nombre,str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False



def pedir_nombre(msg):
    nombre=""
    while (validar_nombre(nombre) == False):
        nombre= input(msg)
    #fin while
    return nombre
#fin pedir nombre

def agregar_datos(ruta_archivo,contenido,modo):
    archivo=open(ruta_archivo,modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(ruta_archivo):
    archivo=open(ruta_archivo,"r")
    datos=archivo.read()
    archivo.close()
    return datos

def guardar_datos(nombre_archivo,contenido,modo):
    archivo=open(nombre_archivo, modo)
    contenido=archivo.read()
    archivo.close()
    return contenido

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido=archivo.read()
    return contenido

def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista=archivo.readlines()
    archivo.close()
    return lista


def validar_sexo(sexo):
    if (isinstance(sexo,str)):
        if (sexo=="Femenino" or sexo=="Masculino"):
                return True
        else:
            return False
    else:
        return False

def pedir_sexo(msg):
    sexo=""
    while(validar_sexo(sexo)==False):
        sexo=input(msg)
    return sexo


def validar_mes(mes):
     if (isinstance(mes,str)):
         if (mes=="Enero" or mes=="Febrero" or mes=="Marzo" or mes=="Abril" or mes=="Mayo" or mes=="Junio" or mes=="Julio" or mes=="Agosto" or mes=="Setiembre" or mes=="Octubre" or mes=="Noviembre" or mes=="Diciembre"):
                 return True
         else:
             return False
     else:
         return False

def pedir_mes(msg):
    mes=""
    while (validar_mes(mes)==False):
        mes=input(msg)
    return mes


def validar_almuerzo(almuerzo):
    if (isinstance(almuerzo,str)):
        if (almuerzo=="Arroz con pato" or almuerzo=="Aji de gallina" or almuerzo=="Lomo saltado"):
               return True
        else:
            return False
    else:
        return False

def pedir_almuerzo(msg):
    almuerzo=""
    while (validar_almuerzo(almuerzo)==False):
        almuerzo=input(msg)
    return almuerzo

def validar_maravilla(maravilla):
    if (isinstance(maravilla,str)):
        if (len(maravilla)>=4):
            return True
            if (maravilla=="Machupichu" or maravilla=="La gran muralla china" or maravilla=="Chichen itza" or maravilla=="Cristo Redentor" or maravilla=="coliseo romano"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def pedir_maravilla(msg):
    maravilla=""
    while (validar_maravilla(maravilla)==False):
        maravilla=input(msg)
    return maravilla

def validar_oceano(oceano):
    if (isinstance(oceano,str)):
        if (len(oceano)>=4):
            return True
            if (oceano=="Pacifico" or oceano=="Artico" or oceano=="Antartico"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def pedir_oceano(msg):
    oceano=""
    while (validar_oceano(oceano)==False):
        oceano=input(msg)
    return oceano

def validar_suyos(suyos):
    if (isinstance(suyos,str)):

        if (suyos=="Collasuyo" or suyos=="Antisuyo" or suyos=="Chinchaysuyo" or suyos=="Contisuyo"):
                return True

        else:
            return False
    else:
        return False

def pedir_suyos(msg):
    suyos=""
    while (validar_oceano(suyos)==False):
        suyos=input(msg)
    return suyos

def validar_vocales(vocales):
    if (isinstance(vocales,str)):
        if (len(vocales)== 1):
            return True
            if (vocales=="a" or vocales=="e" or vocales=="i" or vocales=="o" or vocales=="u"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def pedir_vocales(msg):
    vocales=""
    while (validar_vocales(vocales)==False):
        vocales=input(msg)
    return vocales
