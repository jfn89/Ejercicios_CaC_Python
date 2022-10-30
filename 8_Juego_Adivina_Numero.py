'''Ingresar un numero de 1 a 100 hasta 5 veces y 
tratar de adivinar el numero de la máquina.
La maquina debe dar pistas si el numero ingresado
es mayor o menor que el de la maquina, y si la persona
acierta escribi un mensaje de Ganaste Campeon/a!!!!!'''

from random import Random, randrange


print("Adivina el número")
print(" ")
print("Tenés 5 intentos para adivinar el número.")
print(" ")
NumeroMaquina= randrange(1,101)
print(NumeroMaquina)
NumeroUsuario = 0
Contador = 1

while (Contador <= 5) and (NumeroUsuario != NumeroMaquina):
    NumeroUsuario = int(input("Ingresa un número del 1 al 100: "))
    if NumeroUsuario > NumeroMaquina:
        print("El número que ingresaste es mayor.")
    elif NumeroUsuario < NumeroMaquina:
        print("El número que ingresaste es menor.")
    Contador = Contador + 1 

if NumeroUsuario == NumeroMaquina:
    print("Ganaste Campeón/Campeona!!!")
else:
    print("Mejor suerte la próxima vez, el número secreto era ", NumeroMaquina, ".")
