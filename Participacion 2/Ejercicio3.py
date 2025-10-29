#Ejercicio 3

numero = int(input("Ingrese el numero entero del cual quiera la tabla de multiplicar de multiplos pares: "))
resultado = 0

for i in range(2, numero + 1):
    if i % 2 == 0:
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")