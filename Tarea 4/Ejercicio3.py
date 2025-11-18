# 3.- Haz un programa que pida al usuario una contraseña. Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.

contra = input("Ingrese una contraseña(Debe contener al menos 8 caracteres, una mayuscula y un numero)")
mayus = 0
numero = 0

for mayuscula in contra:
    if ((mayuscula.isupper()) == True):
        mayus += 1

for num in contra:
    if ((num.isdigit()) == True):
        numero += 1

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