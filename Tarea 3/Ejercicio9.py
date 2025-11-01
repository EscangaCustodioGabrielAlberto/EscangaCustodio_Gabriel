# Pide una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%.

cantidad = int(input("Ingrese la cantidad de productos que desea pagar: "))
producto = 1
precio = 0
suma = 0
totalIVA = 0

while (producto <= cantidad):
     precio = float(input(f"Ingrese el precio del producto {producto}: "))
     suma += precio
     producto += 1

totalIVA = suma * 1.16

print(f"La suma de sus {producto} productos mas el 16% de IVA es de: {round(totalIVA, 2)}")