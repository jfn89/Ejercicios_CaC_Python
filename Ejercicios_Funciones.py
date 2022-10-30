# Ejercicio 1

'''
Hacer un funcion que reciba dos parametros numericos enteros no necesariamente ordenados, y 
retorne la suma de los numeros enteros que hay entre el primero y el segundo (incluidos ambos)
'''

# def sumar_rango (num1,num2):
#     rango = (0)
#     if num1 > num2:
#         rango = range(num2, num1 + 1)
#     else:
#         rango = range(num1, num2 + 1)
#     suma = sum(rango, 0,) 
#     return suma

# num1 = int(input("Ingrese un número: "))
# num2 = int(input("ingrese otro número: "))
# numeros = sumar_rango (num1, num2)
# print(numeros)

# Ejercicio 2

'''
Hacer una funcion que reciba un numero entero positivo y devuelva el factorial del mismo
Ejemplo: Si ingresa el 8 la funcion debe retornar
el resultado de 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 
'''

# def factorial_numero (num):
#     contador = 1
#     factorial = 1
#     while contador  <= num:
#         factorial = contador * factorial
#         contador = contador + 1
#     return factorial

# print(factorial_numero(8))

# Ejercicio 3

'''
Hacer una funcion que reciba un arreglo de numeros enteros y retorne la suma de esos numeros
numeros = [34, 23, 54, 75, 23]
La funcion debe retornar la suma de los numeros del arreglo
len(numeros)
'''

# def suma_array(numeros):
#     suma = sum(numeros, 0)
#     return suma

# arreglo_numeros = [34, 23, 54, 75, 23]
# print (suma_array(arreglo_numeros))


# def suma_arreglo (numeros):
#     numeros = list(numeros)
#     suma = 0
#     for x in range(0, len(numeros),1):
#         suma = suma + numeros[x]
#     return suma

# arreglo_numeros = [34, 23, 54, 75, 23]
# print (suma_arreglo(arreglo_numeros))

# Ejercicio 4

'''
Hacer una funcion que reciba dos numeros y devuelva el mayor. Si los valores ingresados son iguales,
devolver ese valor.
'''

# def mayor(num1, num2):
#     if num1 > num2:
#         return num1
#     elif num1 < num2:
#         return num2
#     else:
#         return num1

# print(mayor(5,5))

# Ejercicio 5

'''
Hacer una funcion que reciba dos numeros y devuelva el menor. Si los valores ingresados son iguales,
devolver ese valor.
'''

# def menor(num1, num2):
#     if num1 > num2:
#         return num2
#     elif num1 < num2:
#         return num1
#     else:
#         return num1

# print(menor(5,5))

# Ejercicio 6
'''
Hacer una función que reciba una cadena de caracteres y si la cadena contiene o no la letra  "a". 
La funcion debe devolver True o False. 
1) en principio con una estructura cíclica.
2) buscar si existe una función en python que haga lo mismo.
'''
def buscador_a (cadena):
    for i in cadena:
        if i == "a":
            return True
        elif i == "A":
            return True
        elif i == "á":
            return True
        elif i == "Á":
            return True
    return False

cad = input("Ingrese el texto en el que quiere buscar un caracter: ")
print(buscador_a(cad))
'''
# Devuelve la posición de la primer coincidencia
cadena= "Hola como estas"
print(cadena.find("a"))

'''

# Ejercicio 7
'''
Hacer una función que reciba una cadena de caracteres y un caracter como parámetros, y determine 
cuantas veces aparece ese caracter en la cadena.
'''
def contador_caracteres (cadena,caracter):
    contador = 0
    for i in cadena:
        if i == caracter:
            contador = contador + 1 
    return contador
            

cad = input("Ingrese el texto en el que quiere buscar un caracter: ")
car = input("Ingrese el caracter que desea buscar: ")
print(contador_caracteres(cad,car))

# Ejercicio 8
'''
Hacer una función que reciba una cadena de caracteres y devuelva cuantas vocales hay en dicha cadena
'''
def contador_vocales (cadena):
    contador = 0
    for i in cadena:
        if i in "aAáÁeEéÉiIíÍoOóÓuUúÚ":
            contador = contador + 1
    return contador

cad = input("Ingrese el texto en el que quiere buscar un caracter: ")
print(contador_vocales(cad))