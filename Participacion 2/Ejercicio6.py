# Ejercicio 6
numero = int(input("Ingrese un numero entero para generar la tabla de multiplicar: "))
resultado = 0
mayor50 = 0
menor50 = 0
igual50 = 0

for i in range(1, 11):
    resultado = numero * i
    if resultado > 50:
        mayor50 += 1
    elif resultado < 50:
        menor50 += 1
    else:
        igual50 += 1

    print(f"{numero} X {i} = {resultado}")

print(f"La cantidad de resultados mayores a 50 es de: {mayor50}")
print(f"La cantidad de resultados menores a 50 es de: {menor50}")
print(f"La cantidad de resultados iguales a 50 es de: {igual50}")