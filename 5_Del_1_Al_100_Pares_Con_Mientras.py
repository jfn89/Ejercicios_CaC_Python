'''Hacer un algoritmo que obtenga los n�mero 
pares del 1 al 100 usando la instruccion mod
Para realizar no obligatorio'''

Contador = 1

while Contador <= 100:
    if Contador % 2 == 0:
        print(Contador)
    Contador = Contador + 1
