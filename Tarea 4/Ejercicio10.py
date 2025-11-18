#10

lista_nombres = []

for i in range(5):
    nombre = input("Ingrese un nombre: ")
    lista_nombres.append(nombre)

nombre_buscado = input("Ingrese el nombre que desea buscar: ")

esta_nombre = (lista_nombres.count(nombre_buscado))

if (esta_nombre >= 1):
    print("Encontrado")
else:
    print("No encontrado")

