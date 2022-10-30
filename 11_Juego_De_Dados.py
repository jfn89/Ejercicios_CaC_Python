# Juego de dados
'''
Se tiran 5 dados por ronda
Puntuación
1- Los 5 dados iguales suma 20 puntos
2- 4 dados iguales suma 12 puntos
3- 3 dados iguales y un par suma 9 puntos
4- 3 dados iguales suma 6 puntos
5- 2 pares de dados iguales suma 5 puntos
6- 1 par de dados iguales suma 2 puntos
Se juegan 5 rondas
'''
from random import randint

ronda = 1
dados = []
puntaje_total= 0
while ronda <=5:
    print(f"Ronda #{ronda}")
    tirar_dados = input("Tirar dados? s/n: ")
    if tirar_dados == "n":
        print("Daleee.... tirá los dados...")
        continue
    for i in range(5):
        dados.append(randint(1,6))
    print(f"Tu tirada es: {dados}")
    trio = 0
    par1 = 0
    par2 = 0
    puntaje = 0
    for dado in dados:
        if dados.count(dado) == 5:
            print(f"Felicitaciones todos iguales: ({dado}). Sumas 20 puntos")
            puntaje = puntaje + 20
            break
        elif dados.count(dado) == 4:
            print(f"Felicitaciones 4 dados iguales: ({dado}). Sumas 12 puntos")
            puntaje = puntaje + 12
            break
        elif dados.count(dado) == 3:
            if trio == 0:
                print(f"Sacaste un trío: ({dado})")
                trio = dado
        elif dados.count(dado) == 2:
            if par1 == 0:
                print(f"Sacaste un par: ({dado})")
                par1 = dado
            elif par1 != dado and par2 == 0:
                print(f"Sacaste un par: ({dado})")
                par2 = dado
    if par1 != 0 and par2 != 0:
        print(f"Doble par sumas 5 puntos")
        puntaje = puntaje + 5
    elif par1 != 0:
        if trio != 0:
            print(f"Trío y par sumas 9 puntos")
            puntaje = puntaje + 9 
        else:
            print(f"Par simple sumas 2 puntos")
            puntaje = puntaje + 2
    else:
        if trio != 0:
            print(f"Trío simple sumas 6 puntos")
            puntaje = puntaje + 6       
    print(f"En esta ronda sumaste {puntaje} puntos")
    ronda = ronda +1
    puntaje_total = puntaje_total + puntaje
    dados.clear()

print(f"Sumaste en total {puntaje_total} puntos")
