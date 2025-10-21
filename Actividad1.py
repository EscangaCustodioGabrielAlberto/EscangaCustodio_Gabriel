#Haz un programa que solicite al usuario la base y la altura de un rectangulo y calcula su area
# y perimetro

base = int(input("Ingresa la base del rectangulo: "))
altura = int(input("Ingresa la altura del rectangulo: "))

area = base * altura
perimetro = (base * 2) + (altura * 2)

print(f"El area del rectangulo es de: {area}")
print(f"El perimetro del rectangulo es de: {perimetro}")
