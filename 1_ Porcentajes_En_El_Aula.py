"""Hacer un algoritmo que reciba la cantidad de hombres y la cantidad de mujeres que hay en un curso. 
Obtener el total de alumnos, el porcentaje de hombres y el porcentaje de mujeres, y mostrarlo por pantalla. """

Alumnos = int(input("¿Cuántos hombres hay en la clase?"))
	
Alumnas = int(input("¿Cuántas mujeres hay en la clase?"))
	
TotalEstudiantes = Alumnos + Alumnas
print("En la clase hay ", TotalEstudiantes, " estudiantes.")

PorcentajeAlumnos = (Alumnos * 100) / TotalEstudiantes
print("El ", PorcentajeAlumnos, "% son Hombres.")

PorcentajeAlumnas = (Alumnas * 100) / TotalEstudiantes
print("El ", PorcentajeAlumnas, "% son Mujeres.")