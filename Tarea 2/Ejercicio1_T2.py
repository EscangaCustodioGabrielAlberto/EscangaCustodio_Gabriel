# Haz un programa en Python que pida tres calificaciones y calcule su promedio con dos decimales.

calificacion1 = float(input("Ingrese la primera calificacion: "))
calificacion2 = float(input("Ingrese la segunda calificacion: "))
calificacion3 = float(input("Ingrese la tercera calificacion: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

print(f"Tu promedio es de: {round(promedio, 2)}")
