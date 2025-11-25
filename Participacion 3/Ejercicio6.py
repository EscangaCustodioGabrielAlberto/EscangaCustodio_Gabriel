#6.- Haz un programa que pida "Nombre" y "Calificaciones". Posteriormente calcula el promedio general, calificación mayor, calificación menor y muestra el nombre del mejor alumno. Agrega 5 nombres y calificaciones.

diccionario_alumnos = {}

for i in range(5):
    nombre = input("Introduce el nombre del alumno: ")
    calificacion = float(input(f"Introduce la calificación de {nombre}: "))
    while(calificacion < 0 or calificacion > 10):
        calificacion = float(input(f"Calificación inválida. Introduce la calificación de {nombre} entre 0 y 10: "))
    
    diccionario_alumnos[nombre] = calificacion

suma_calificaciones = sum(diccionario_alumnos.values())
promedio = suma_calificaciones / len(diccionario_alumnos)
print(f"El promedio general de los alumnos es: {promedio}")
print(f"La calificacion mayor es: {len(diccionario_aprobados)}")
print(f"La calificacion menor es: {len(diccionario_reprobados)}")