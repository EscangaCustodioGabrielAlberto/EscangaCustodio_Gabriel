# 4.- Haz un programa que pida un texto y una palabra. Si la palabra está en el texto, muestra cuántas veces aparece.

texto = input("Ingresa un texto: ")
palabra = input("Ingresa la palabra que deseas buscar en el texto: ")
contador = texto.lower().count(palabra)

if contador == 0:
    print(f"La palabra '{palabra}' no se encuentra en el texto.")
else:
    print(f"La palabra '{palabra}' se encuentra {contador} veces en el texto.")