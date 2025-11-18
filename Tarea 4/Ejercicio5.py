#5.- Pide al usuario una lista de palabras (separadas por comas, por ejemplo Hola, Mario, Python, Programación). Elimina los elementos repetidos y los que sean menores a 3 letras. Muestra la nueva lista e imprímela en pantalla. 
palabras = input("Ingresa una lista de palabras(Separa las palabras con comas y termine la ultima palabra con un punto final por favor): ")
while not palabras.endswith("."):
    palabras = input("LA LISTA DEBE TERMINAR CON UN PUNTO. Ingrese la frase con un punto al final: ")

lista_palabras = []
palabra = ""

# En este ciclo for si la letra es diferente a un espacio o a un punto, se sumara a la variable "palabra", cuando el caracter sea un espacio o un punto, la palabra se añadira a la lista_frase solo si la longitud de la cadena es mayor a 5, y luego limpiara la variable para que no se junten las palabras anteriores
for letra in palabras:
    if (letra != " ") and (letra != ".") and (letra != ","):
        palabra = palabra + letra
    else:
        if (len(palabra)) > 2:
            lista_palabras.append(palabra.lower())
            palabra = ""
        else:
            palabra = ""

lista_sin_duplicados = set(list(lista_palabras))

print("Esta es la lista sin elementos duplicados y sin palabras menores a 3 letras:")
print(lista_sin_duplicados)
    