# Haz un programa en Python que calcule el área de un círculo a partir de su radio.
import math

radio = float(input("Ingrese el radio del circulo: "))

areaCirculo = math.pi * (radio ** 2)

print(f"El area del circulo es: {areaCirculo}")