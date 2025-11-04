#Haz un programa que solicite al usuario dos numeros, y muestre su suma, resta, multiplicacion
#y division

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"La suma de los numeros {num1} y {num2} es: {suma}")
print(f"La resta de los numeros {num1} y {num2} es: {resta}")
print(f"La multiplicacion de los numeros {num1} y {num2} es: {multiplicacion}")
print(f"La division de los numeros {num1} y {num2} es: {division}")
