# 1.- Pide una frase, divídela en palabras y guarda una lista solo las que tengan más de 5 letras. Muestra la lista resultante.

#Aqui pedi la frase y puse que debe tener un punto final, ya que asi puedo guardar la ultima palabra con el ciclo for
frase = input("Ingresa una frase(Termine la frase con un punto final por favor): ")
while not frase.endswith("."):
    frase = input("LA FRASE DEBE TERMINAR CON UN PUNTO. Ingrese la frase con un punto al final: ")

lista_frase = []
palabra = ""

# En este ciclo for si la letra es diferente a un espacio o a un punto, se sumara a la variable "palabra", cuando el caracter sea un espacio o un punto, la palabra se añadira a la lista_frase solo si la longitud de la cadena es mayor a 5, y luego limpiara la variable para que no se junten las palabras anteriores
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

