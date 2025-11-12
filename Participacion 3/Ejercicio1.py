#1.- Pide nombres hasta que el usuario escriba la palabra "Fin". Al final muestra cuantos nombres ingresó, y cuál es el primero y el último.
lista_nombres = []

while True:
    nombre = input("Ingresa un nombre o ingresa 'Fin' para terminar: ")
    if nombre == "Fin":
        break
    lista_nombres.append(nombre)

print(f"La cantidad de nombres ingresados fue: {len(lista_nombres)}")
print(f"El primer nombre es: {lista_nombres[0]}")
lista_nombres.reverse()
print(f"El ultimo nombre es: {lista_nombres[0]}")