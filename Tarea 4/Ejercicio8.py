#8

palabra = input("Ingrese una palabra: ")

if (palabra.lower().startswith(("a", "e", "i", "o", "u"))):
    print("La palabra inicia con una vocal")
else:
    print("La palabra NO inicia con una vocal")