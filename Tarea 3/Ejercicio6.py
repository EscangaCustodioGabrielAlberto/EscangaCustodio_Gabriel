# Haz un programa que pida un número, y muestre si es primo o no.

numero = int(input("Ingrese un numero entero para saber si es primo o no: "))
contDivisiones = 0

#Hice el for para saber cuantos divisores tiene el numero.
for i in range(1, numero + 1):
    if (numero % i == 0):
        contDivisiones += 1

#Como los numeros primos solo tienen dos divisores, puse el contador para comparar si solo tiene dos divisores el numero ingresado.
if (contDivisiones == 2):
    print(F"{numero} es un numero primo.")
else:
    print(f"{numero} NO es un numero primo.")