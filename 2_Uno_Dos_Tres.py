'''Hacer un algoritmo donde el usuario ingrese un número del 1 al 3, es decir, 1 o 2 o 3, e 
imprimir por pantalla el numero en texto, por ejemplo si ingresa el 1 imprimir en pantalla Uno'''

NumeroIngresado = int(input("Ingrese un número del 1 al 3: "))

if NumeroIngresado == 1:
    print ("Uno")
elif NumeroIngresado == 2:
    print ("Dos")
elif NumeroIngresado == 3: 
    print("Tres")
else:
    print ("El número ingresado se encuentra fuera del rango solicitado.")