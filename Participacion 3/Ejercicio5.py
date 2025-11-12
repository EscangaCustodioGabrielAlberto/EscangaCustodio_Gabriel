#5.- Haz un programa que pida 10 números, y crea una nueva lista sin duplicados.
lista_numeros = []
lista_numeros_sin_duplicados = []

for i in range(10):
    numero = float(input("Ingresa un numero: "))
    lista_numeros.append(numero)

lista_numeros_sin_duplicados = set(list(lista_numeros))

print(f"La lista de numeros sin duplicados es: {lista_numeros_sin_duplicados}")