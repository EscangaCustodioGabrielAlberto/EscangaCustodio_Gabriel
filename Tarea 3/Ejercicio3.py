# Haz un programa que pida un número y muestre si es divisible entre 2, 3 o ambos.

numero = int(input("Ingrese un numero entero para saber si es divisible ente 2, 3 o ambos: "))

if (numero % 2 == 0) and (numero % 3 == 0):
    print(f"{numero} es divisible entre 2 y 3.")
elif (numero % 3 == 0):
    print(f"{numero} es divisible entre 3.")
elif (numero % 2 == 0):
    print(f"{numero} es divisible entre 2.")
else:
    print(f"{numero} NO es divisible entre 2 ni entre 3.")

    