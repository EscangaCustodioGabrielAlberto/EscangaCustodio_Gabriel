# Haz un programa que solicite números al usuario hasta que ingrese un cero. Al final, imprime cuántos números positivos y negativos introdujo.

numero = float(input("Ingrese un numero diferente a 0: "))
contPosi = 0
contNega = 0

if numero < 0:
    contNega += 1
else:
    contPosi += 1

while numero != 0:
    numero = float(input("Ingrese un numero diferente a 0: "))
    if numero < 0:
        contNega += 1
    elif numero > 0:
        contPosi += 1
    else:
        print("Numero cero ingresado.")

print(f"La cantidad de numeros negativos fueron: {contNega}")
print(f"La cantidad de numeros positivos fueron: {contPosi}")