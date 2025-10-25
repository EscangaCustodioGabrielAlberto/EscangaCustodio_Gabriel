# Haz un programa en Python que pida tres números y muestre si se cumple la expresión A < B < C 

numeroA = int(input("Ingrese el primer nuemro: "))
numeroB = int(input("Ingrese el segundo nuemro: "))
numeroC = int(input("Ingrese el tercero nuemro: "))

print(f"Se cumple la condicion A < B < C? {numeroA < numeroB < numeroC}")