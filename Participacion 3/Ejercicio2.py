#2.- Pide números hasta que el usuario escriba 0. Guarda los pares en una lista y los impares en otra. Al final, muestra cuantos números hay en cada lista. Ordena la lista en orden ascendente y recorre las listas para mostrar cada número uno por uno.
lista_par = []
lista_impar = []

while True:
    numero = int(input("Ingrese un numero entero, o ingrese '0' para terminar: "))
    if (numero % 2 == 0) and (numero != 0):
        lista_par.append(numero)
    elif (numero % 2 != 0) and (numero != 0):
        lista_impar.append(numero)
    else:
        break

print(f"En la lista de pares hay {len(lista_par)} elementos")
lista_par.sort()
for numPar in lista_par:
    print(numPar)

print(f"En la lista de impares hay {len(lista_impar)} elementos")
lista_impar.sort()
for numImpar in lista_impar:
    print(numImpar)