# Ejercicio 1

'''
Imprimir los números pares del 2 al 100 pero con paso 1    
'''

Contador = 1

while Contador <= 100:
    if Contador % 2 == 0:
        print(Contador)
    Contador = Contador + 1

# Ejercicio 2

'''
Algoritmo donde el usuario ingresa edades, y el ingreso finaliza cuando el usuario
ingresa el número de edad 999. Finalmente el programa debe informar la cantidad
de edades ingresadas, la suma total de la edades, el promedio de las edades ingresadas
'''

contador = 0
edad = 0
edad_ingresada= 0

while edad_ingresada != 999:
    edad_ingresada = int(input("Por favor ingrese un número (al ingresar 999 termina el proceso): "))
    if edad_ingresada !=999:
        edad = edad + edad_ingresada
        contador += 1

print(f"Ingresaste {contador} edades.")
print(f"La suma de las edades ingresadas es {edad}.")
print(f"El promedio de edades es {edad/contador} ")


# Ejercicio 3

'''
Hacer un algoritmo que solicite al usuario el ingreso de 2 numeros enteros distintos, el primero
menor que el segundo, e imprima por pantalla la suma de los numeros enteros que hay entre
el primero y el segundo
'''

num1 = int(input("Ingrese un número: "))
num2 = int(input("ingrese un número mayor al anterior: "))

rango = range(num1, num2 + 1)
suma = sum(rango, 0)
print(suma)

# Ejercicio 4

'''
Hacer un algoritmo que solicite al usuario el ingreso de 2 numeros enteros no necesariamente
ordenados, e imprima por pantalla la suma de los numeros enteros que hay entre
el primero y el segundo
'''

num1 = int(input("Ingrese un número: "))
num2 = int(input("ingrese otro número: "))

rango = (0)

if num1 > num2:
    rango = range(num2, num1 + 1)
else:
    rango = range(num1, num2 + 1)

suma = sum(rango, 0,) 
print(suma)