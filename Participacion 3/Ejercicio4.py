#4.- Pide una frase y cuenta cuántas vocales usa (a, e, i, o, u).
frase = input("Ingresa una frase: ")
frase.lower()
vocalA = frase.count("a")
vocalE = frase.count("e")
vocalI = frase.count("i")
vocalO = frase.count("o")
vocalU = frase.count("u")
vocales = vocalE + vocalA + vocalI + vocalO + vocalU
print(f"La cantidad de vocales de la frase es de: {vocales}")