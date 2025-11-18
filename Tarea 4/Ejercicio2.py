# 2.- Haz un programa que pida una frase y cuenta cuántas veces aparece cada palabra. Por ejemplo "Esta es una prueba", "Esta" aparece una vez, "es", una vez, "una", una vez, etc...

frase = input("Ingresa una frase(Termine la frase con un punto final por favor): ")
while not frase.endswith("."):
    frase = input("LA FRASE DEBE TERMINAR CON UN PUNTO. Ingrese la frase con un punto al final: ")

lista_frase = []
lista_repetida = []
palabra = ""
diccionario_palabras = {}

for letra in frase.lower():
    if (letra != " ") and (letra != "."):
        palabra = palabra + letra
    else:
        lista_frase.append(palabra)
        palabra = ""

for palabra_repetida in lista_frase:
    veces = lista_frase.count(palabra_repetida)
    diccionario_palabras[palabra_repetida] = veces
    
print("Lista de palabras y cuantas veces se repiten en la frase: ")
for palabra, veces in diccionario_palabras.items():
    print(f"{palabra}: {veces}")

