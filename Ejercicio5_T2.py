# Haz un programa en Python que pida un precio y muestre el total con IVA del 16%.

precio = float(input("Introduce el precio del producto: "))

precioIVA = precio * 1.16

print(f"El precio del producto con el IVA (16%) seria: ${round(precioIVA, 2)}")