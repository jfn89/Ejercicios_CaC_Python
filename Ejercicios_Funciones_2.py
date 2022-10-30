# Ejercicio 1
''' Hacer un algoritmo que imprima lo siguiente: 
*****
Luego convertirlo en funcion
'''

for i in range(0,5):
    print("*", end="")
print ("")

def asteriscos(n):
    cadena = ""
    for i in range (0,n):
        cadena = cadena + "*"
        
    return cadena

nro = int(input("Ingresa la cantidad de asteriscos que querés imprimir: "))
print(asteriscos(nro))

# Ejercicio 2

'''
Hacer una funcion que reciba como argumento, un caracter y un número e imprima ese caracter n veces. 
Puede hacer ingresar con input los valores y luego invocar a la función.
'''
def caracteres(c,n):
    cadena = ""
    for i in range (0,n):
        cadena = cadena + c   
    return cadena

caracter = input("Ingresa el caracter que querés imprimir: ")
nro = int(input("Ingresa la cantidad de caracteres que querés imprimir: "))
print(caracteres(caracter,nro))

# Ejercicio 3
'''
Hacer una funcion que le envio un caracter y un numero y devuelve el cuadrado dibujado
'''   

def patron (car, num):
    cadena = ""
    cuadrado = ""
    for i in range(0,num):
        cadena= (car + " ") * num
        cuadrado = cuadrado + (cadena + "\n" ) 
    return cuadrado

caracter = input("Ingresa el caracter que querés imprimir: ")
nro = int(input("Ingresa la cantidad de caracteres que querés imprimir: "))
print(patron(caracter,nro))
print(patron("*",5))
