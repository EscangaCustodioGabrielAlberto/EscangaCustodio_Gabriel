#5.-

lista_calificaciones = []
suma_calificaciones = 0

for cali in range(1, 6):
    calificacion = float(input(f"Ingrese la calificacion {cali}: "))
    while not ((calificacion >= 1) and (calificacion <= 10)):
        calificacion = float(input(f"Calificacion fuera de rango (del 1 al 10). Ingrese la calificacion {cali}: "))


for calificacion in lista_calificaciones:
    suma_calificaciones = suma_calificaciones + calificacion

promedio = (suma_calificaciones / len(lista_calificaciones))
print(f"El promedio es de {promedio.round(2)}")

if (promedio == 10):
    print("Excelente")
elif (promedio < 10) and (promedio >= 6):
    print("Aprobado")
else:
    print("Reprobado")