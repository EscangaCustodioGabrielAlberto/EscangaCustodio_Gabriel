# Haz un programa en python 

numero = int(input("Ingrese un numero entero: "))
contPar = 0
contImpar = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        contPar += 1
        print(i)
    else:
        contImpar += 1
        print(i)

print(f"Del numero 1 al {numero}, hay {contPar} numeros pares y {contImpar} numeros impares.")