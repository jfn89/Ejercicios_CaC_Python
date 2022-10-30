'''Hacer un Algoritmo en el que el usuario ingrese dos números, y el algoritmo debe mostrar por pantalla
si el primero número es mayor que el segundo, o si el segundo número es mayor que el primero, 
o bien si son iguales'''

Num1 = int(input("Ingrese un número: "))
Num2 = int(input("Ingrese otro número: "))

if Num1 > Num2:
    print("El primer número ingresado es mayor al segundo.")
elif Num1 < Num2:
    print("El primer número ingresado es menor al segundo.")
else:
    print("Los números ingresados son iguales.")
