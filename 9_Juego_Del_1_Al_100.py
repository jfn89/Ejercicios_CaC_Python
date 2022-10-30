'''Hacer un algoritmo en el que ud juegue contra la maquina.
Ud tiene que adivinar un numero de 1 a 100 que eligirá al azar la maquina, tendra solo 5 chances.
La máquina debe guiarlos con es mayor o es menor que el que eligirá, o bien decir, Ud ha ganado. '''

from random import Random, randrange

#Proceso JuegoAdivinaNumero

'''print("Adivina el número")
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
    print("Mejor suerte la próxima vez, el número secreto era ", NumeroMaquina, ".")'''


#Dificil: Hacer lo mismo pero con el repetir

'''print("Adivina el número")
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
    print("Mejor suerte la próxima vez, el número secreto era ", NumeroMaquina, ".")'''


#Ultradificil: Que pasa si queremos competir contra la maquina, a ver quien gana mas partidos en 3.

print("Adivina el número")
print(" ")
print("Tenés 5 intentos para adivinar el número.")
print(" ")

Contador = 1
ContadorMaquina = 1
Partida = 1
GanoUsuario = 0
GanoMaquina = 0

while Partida <= 3:
    NumSecreto= randrange(1,101)
    NumeroUsuario = 0
    while (Contador <= 5) and (NumeroUsuario != NumSecreto):
        NumeroUsuario = int(input("Ingresa un número del 1 al 100: "))
        if NumeroUsuario > NumSecreto:
            print("El número que ingresaste es mayor.")
        elif NumeroUsuario < NumSecreto:
            print("El número que ingresaste es menor.")
        Contador = Contador + 1 
    if NumeroUsuario == NumSecreto:
        GanoUsuario = GanoUsuario + 1
        print("Ganaste Campeón/Campeona!!!")
    else:
        print("Mejor suerte la próxima vez, el número secreto era ", NumSecreto, ".")
    Partida = Partida + 1 
    Contador = 1

while Partida <= 3:
    NumSecreto = randrange(1,101)
    NumeroMaquina = 0
    while (ContadorMaquina <= 5) and (NumeroUsuario != NumSecreto):
        NumeroMaquina = randrange (1,101)
        if NumeroMaquina != NumSecreto:
            ContadorMaquina = ContadorMaquina + 1
        else:
            GanoMaquina = GanoMaquina + 1
    Partida = Partida + 1 
    ContadorMaquina = 1

if GanoUsuario > GanoMaquina:
    print("Felicidades! Me ganaste por ", GanoUsuario, " a ", GanoMaquina, ".")
elif GanoUsuario < GanoMaquina:
	print ("Mejor suerte la próxima vez!, te gané por ", GanoMaquina, " a ", GanoUsuario, ".")
else:
    print("Esta vez empatamos.")