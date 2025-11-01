# Haz un programa que pida una edad, y dependiendo del rango, muestre una categoría:
    #  - Menor de 13 años -> "Niño"
    #  - 13 a 17 años -> "Adolescente"
    #  - 18 a 64 años -> "Adulto"
    #  - 65 o más -> "Adulto mayor"

edad = int(input("ingrese su edad: "))

if (edad < 13):
    print("Eres un niño.")
elif (edad >= 13) and (edad <= 17):
    print("Eres un adolescente.")
elif (edad >= 18) and (edad <= 64):
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")