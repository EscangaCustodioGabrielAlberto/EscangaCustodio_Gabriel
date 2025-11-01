# Haz un programa que sume todos los números impares del 1 al 50.
suma = 0

#Para saber si era impar, puse en la condicional del if que solo los sumara si el modulo de i entre 2 era diferente de 0
for i in range(1, 51):
    if (i % 2 != 0):
        suma += i

print(f"La suma de todos los numero impares del 1 al 50 es: {suma}")