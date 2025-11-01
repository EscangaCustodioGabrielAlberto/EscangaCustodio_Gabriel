# Haz un programa que calcule cuántos números del 1 al 100 son divisibles entre 3 y entre 5.

contador = 0

for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        contador += 1

print(F"La cantidad de numeros del 1 al 100 que se pueden dividir entre 3 y 5 son: {contador}")