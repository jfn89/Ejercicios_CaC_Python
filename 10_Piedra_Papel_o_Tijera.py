#PiedraPapeloTijera

from random import randrange


print("Juego de Piedra papel o tijeras contra la PC")
print("Para jugar ingrese los numeros del 1 al 3")
	
suma1= 0
suma2= 0

PiedraPapelTijera = {1:"Piedra", 2:"Papel", 3:"Tijera"}

while suma1 < 3 and suma2 < 3 :
    NumUs = int(input("Elija 1. Piedra, 2. Papel, 3. Tijera: "))
    print("Elegiste ", PiedraPapelTijera.setdefault(NumUs))
    
    NumMaq = randrange(1,4)
    print("Tu rival eligió ", PiedraPapelTijera.setdefault(NumMaq))

    if NumUs == NumMaq:
        print("Hay empate, siguen ", suma1, " vs ", suma2, ".")
    elif (NumUs == 1 and NumMaq == 3) or (NumUs == 2 and NumMaq == 1) or (NumUs == 3 and NumMaq == 2):
        suma1 = suma1 + 1
        print("Ganaste!, vas ", suma1, " vs ", suma2, ".")
    else:
        suma2 = suma2 + 1 
        print("Perdiste!, vas ", suma1, " vs ", suma2, ".")

print(" ")
if suma1 == 3:
    print("Ganaste!!!, con un total de ", suma1, " vs ", suma2, ".")
else:
    print("Perdiste... con un total de ", suma1, " vs ", suma2, ".")

print(" ")