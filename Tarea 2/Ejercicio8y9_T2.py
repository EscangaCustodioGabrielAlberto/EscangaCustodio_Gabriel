# Haz un programa en Python que pida tres números y muestre si los tres son iguales

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

print(f"Los tres numeros son iguales? {(num1 == num2) and (num2 == num3)}")
