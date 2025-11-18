# 1.- Pide una frase, divídela en palabras y guarda una lista solo las que tengan más de 5 letras. Muestra la lista resultante.

frase = input("Ingresa una frase(Termine la frase con un punto final por favor): ")
while not frase.endswith("."):
    frase = input("LA FRASE DEBE TERMINAR CON UN PUNTO. Ingrese la frase con un punto al final: ")

lista_frase = []
palabra = ""

for letra in frase:
    if (letra != " ") and (letra != "."):
        palabra = palabra + letra
    else:
        if (len(palabra)) > 5:
            lista_frase.append(palabra)
            palabra = ""
        else:
            palabra = ""
    


print(f"Esta es la lista de palabras mayores a 5 letras: {lista_frase}")

