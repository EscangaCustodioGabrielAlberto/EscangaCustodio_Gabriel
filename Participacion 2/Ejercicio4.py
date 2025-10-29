#Ejercicio 4

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
num4 = float(input("Ingrese el cuarto numero: "))
num5 = float(input("Ingrese el quinto numero: "))
contMayor = 0

if num1 > 10:
    contMayor += 1
    print(num1)

if num2 > 10:
    contMayor += 1
    print(num2)

if num3 > 10:
    contMayor += 1
    print(num3)

if num4 > 10:
    contMayor += 1
    print(num4)

if num5 > 10:
    contMayor += 1
    print(num5)

print(f"La cantidad de numeros que fueron mayores a 10 fueron {contMayor}")