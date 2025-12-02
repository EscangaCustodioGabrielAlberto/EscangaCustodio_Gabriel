#6.-

lista_productos = []

for i in range(1, 11):
    producto = input(f"Ingrese el nombre del producto {i}: ")
    lista_productos.append(producto)

print("Aqui esta la lista de productos ordenados alfabeticamente: ")
print(sorted(list(lista_productos)))