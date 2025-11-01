# Haz un programa que simule una calculadora básica con opciones de suma, resta, multiplicación y división, que se repita hasta que el usuario elija salir.
boton = 0
suma = 0
resta = 0
multi = 0
divi = 0

print("------------Menu------------")
print("Que accion deseas realizar?")
print("1.-Suma")
print("2.-Resta")
print("3.-Multiplicacion")
print("4.-Division")
print("5.-Salir")
boton = int(input("-----> "))

if (boton < 1) or (boton > 5):
    while (boton < 1) or (boton > 5):
        print("Opcion inexistente. Intente de nuevo.")
        boton = int(input("-----> "))

while (boton < 5) and (boton > 0):
    if (boton < 1) or (boton > 5):
        while (boton < 1) or (boton > 5):
            print("Opcion inexistente. Intente de nuevo.")
            boton = int(input("-----> "))
    elif (boton == 1):
        num1 = float(input("Ingrese el primer numero para la suma: "))
        num2 = float(input("Ingrese el segundo numero para la suma: "))
        suma = num1 + num2
        print(f" {num1} + {num2} = {suma}")
    elif (boton == 2):
        num1 = float(input("Ingrese el primer numero para la resta: "))
        num2 = float(input("Ingrese el segundo numero para la resta: "))
        resta = num1 - num2
        print(f" {num1} - {num2} = {resta}")
    elif (boton == 3):
        num1 = float(input("Ingrese el primer numero para la multiplicacion: "))
        num2 = float(input("Ingrese el segundo numero para la multiplicacion: "))
        multi = num1 * num2
        print(f" {num1} x {num2} = {multi}")
    elif (boton == 4):
        num1 = float(input("Ingrese el primer numero para la division: "))
        num2 = float(input("Ingrese el segundo numero para la division: "))
        divi = num1 / num2
        print(f" {num1} / {num2} = {divi}")
    else:
        print("Saliendo del programa... ")

    print("------------Menu------------")
    print("Que accion deseas realizar?")
    print("1.-Suma")
    print("2.-Resta")
    print("3.-Multiplicacion")
    print("4.-Division")
    print("5.-Salir")
    boton = int(input("-----> "))

print("Saliendo del programa...")
print("°°°°°°°°°°°°°°°°°°°°°°°°°")
