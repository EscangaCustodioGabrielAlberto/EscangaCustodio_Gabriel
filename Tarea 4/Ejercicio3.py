# 3.- Haz un programa que pida al usuario una contraseña. Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.

contra = input("Ingrese una contraseña(Debe contener al menos 8 caracteres, una mayuscula y un numero)")
mayus = 0
numero = 0

#Aqui use los ciclos for para verificar si tenia una letra mayuscula, y otro para saber si tenia un numero, utilizando .isupper para las mayusculas y .isdigit para los numeros, si encontraba mayusculas o numeros, estos se iban a guardar en un contador pra utilizarlos como condicional del ciclo while
for mayuscula in contra:
    if ((mayuscula.isupper()) == True):
        mayus += 1

for num in contra:
    if ((num.isdigit()) == True):
        numero += 1

#En este ciclo while, se repetira hasta que la longitud de la contraseña sea igual o mayor que 8, el contador de numeros debe ser diferente a 0 y el contador de mayusculas debe ser diferente a 0
while not ((len(contra) >= 8) and (numero != 0) and (mayus != 0)):
    print("CONTRASEÑA INEFICIENTE")
    contra = input("Ingrese una contraseña(Debe contener al menos 8 caracteres, una mayuscula y un numero)")
    mayus = 0
    numero = 0

    for mayuscula in contra:
        if (mayuscula.isupper()) == True:
            mayus += 1

    for num in contra:
        if (num.isdigit()) == True:
            numero += 1

print("Contraseña valida.")