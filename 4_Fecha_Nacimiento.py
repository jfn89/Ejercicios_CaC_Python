'''Crea un algoritmo que reciba como datos de entrada (ingresado por el ususario),
el nombre,dia de nacimiento(numero) y el numero del mes. Y debe mostrar por pantalla,
en el supuesto que el usuario ingrese Juan Perez(nombre), 5(numero de dia del mes) y 
7 (numero del mes)
El algoritmo deberia devolver el texto como el siguiente:
Ud, Juan Perez, ha nacido el dia 5 de Julio'''

Nombre = input("Ingrese su nombre: ")
DiaNacimiento = int(input("Ingrese su día de nacimiento (en números): "))
MesNacimiento = int(input("Ingrese su mes de nacimiento (en números): "))

Meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 
        9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

print("Ud, ", Nombre, " ha nacido el día ", DiaNacimiento, " de ", Meses.setdefault(MesNacimiento), ".")
