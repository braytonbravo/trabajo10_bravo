import libreria

#1
assert(libreria.validar_vocales("abc")==False)
assert(libreria.validar_vocales("123")==False)
assert(libreria.validar_vocales("a")==True)
print("validar vocales ok")

#2
assert(libreria.validar_suyos("Contisuyo")==True)
assert(libreria.validar_suyos("abcd")==False)
assert(libreria.validar_suyos("mono")==False)
print("validar suyos ok")

#3
assert(libreria.validar_oceano("abc")==False)
assert(libreria.validar_oceano("Antartico")==True)
assert(libreria.validar_oceano("1123")==True)
print("Validar Oceano ok")
#4
assert(libreria.validar_entero_positivo("abc")==False)
assert(libreria.validar_entero_positivo("-123")==False)
assert(libreria.validar_entero_positivo(1)==True)
print("Validar entero ok")
#5
assert(libreria.validar_mes("abc")==False)
assert(libreria.validar_mes("Panama")==False)
assert(libreria.validar_mes("Enero")==True)
print("Validar mes ok")

#6
assert(libreria.validar_almuerzo("abc")==False)
assert(libreria.validar_almuerzo("Manzana")==False)
assert(libreria.validar_almuerzo("Aji de gallina")==True)
print("validar almuerzo ok")
