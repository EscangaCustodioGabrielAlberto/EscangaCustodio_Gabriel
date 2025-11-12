#3.- Haz un programa que pida "Nombre" y "Calificación". Almacena todos estos datos en un diccionario. Posteriormente muestra: Promedio general, cantidad de aprobados y cantidad de reprobados.

diccionario_alumnos = {}
diccionario_aprobados = {}
diccionario_reprobados = {}

alumnos = int(input("Ingrese la cantidad de alumnos que desea ingresar: "))

for i in range(alumnos):
    nombre = input("Introduce el nombre del alumno: ")
    calificacion = float(input(f"Introduce la calificación de {nombre}: "))
    while(calificacion < 0 or calificacion > 10):
        calificacion = float(input(f"Calificación inválida. Introduce la calificación de {nombre} entre 0 y 10: "))

    if calificacion < 6:
        diccionario_reprobados[nombre] = calificacion
    else:
        diccionario_aprobados[nombre] = calificacion
    
    diccionario_alumnos[nombre] = calificacion

suma_calificaciones = sum(diccionario_alumnos.values())
promedio = suma_calificaciones / len(diccionario_alumnos)
print(f"El promedio general de los alumnos es: {promedio}")
print(f"El numero de aprobados es: {len(diccionario_aprobados)}")
print(f"El numero de reprobados es: {len(diccionario_reprobados)}")