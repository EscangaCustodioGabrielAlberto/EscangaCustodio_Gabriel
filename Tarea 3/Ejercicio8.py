#  Pide dos números y muestra todos los números entre ellos que sean múltiplos de 7.

num1 = int(input("Ingresa el primer numero entero: "))
num2 = int(input("Ingresa el segundo numero entero(Diferente al primer numero): "))

if (num1 > num2):
    for i in range(num2, num1 + 1):
        if (i % 7 == 0):
            print(i)
elif (num2 > num1):
    for i in range(num1, num2 + 1):
        if (i % 7 == 0):
            print(i)
else:
    print("Los dos numeros deben de ser diferentes.")