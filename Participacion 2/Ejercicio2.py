# Ejercicio 2

nombre = input("Ingrese su nombre por favor: ")
edad = int(input("Ingrese su edad por favor: "))
faltaEdad = 0

if edad >= 18:
    print(f"Hola {nombre}, tienes la edad suficiente para votar :D")
else:
    for i in range(edad, 18):
        faltaEdad += 1
    print(f"Hola {nombre}, NO tienes la edad suficiente para votar. Te faltan {faltaEdad} años :c")
