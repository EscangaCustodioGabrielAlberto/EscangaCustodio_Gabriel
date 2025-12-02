#4.-

palabra = input("Ingrese una palabra: ")
suma_vocales = 0

for letra in palabra.lower():
    if ((letra == "a") or (letra == "e")):
        suma_vocales += 1
    elif ((letra == "i") or (letra == "o")):
        suma_vocales += 1
    elif (letra == "u"):
        suma_vocales += 1
    
print(f"La cantidad de vocales en la palabra ´{palabra}´ es de: {suma_vocales}")