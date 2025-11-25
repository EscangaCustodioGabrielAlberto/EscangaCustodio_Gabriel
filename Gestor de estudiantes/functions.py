# Función para mostrar las opciones del menu
def mostrar_menu():
    print("Sistema de Gestión de Estudiantes")
    print("1. Agregar estudiante")
    print("2. Mostrar lista completa de estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Buscar estudiante por apellido")
    print("5. Eliminar estudiante")
    print("6. Promedio grupal")
    print("7. Mostrar estudiantes en orden de promedio")
    print("8. Salir")

# Funcion para buscar estudiante por medio del apellido
def buscar_estudiante_apellido(lista_estudiantes):
    apellido_buscar = input("Ingrese el apellido del estudiante que desea buscar: ")
    for estudiante in lista_estudiantes:
        if estudiante['apellido'].lower() == apellido_buscar.lower():
            print(f"Estudiante encontrado: {estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")
            return
    print("Estudiante no encontrado.")

# Funcion para calcular el promedio del grupo
def promedio_grupal(lista_estudiantes):
    suma = 0
    contador = 0
    for estudiante in lista_estudiantes:
        suma = suma + (estudiante['promedio'])
        contador += 1
    
    promedio_grupo = suma / contador
    print(f"El promedio grupal es: {promedio_grupo}")


# Funcion para ordenar estudiantes por promedio (De la calificacion mas alta a la mas baja)
def orden_promedio(lista_estudiantes):
    for estudiante in sorted(list(lista_estudiantes['promedio'])):
        print(estudiante)
    
# Función para agregar un estudiante
def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))
    
    lista_estudiantes.append({"nombre": nombre, "apellido": apellido, "promedio": promedio})
    
    print(f"Estudiante {nombre} {apellido} agregado exitosamente.")

# Función para mostrar lista de estudiantes
def mostrar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes en la lista")
        return
    print("Lista de estudiantes")
    for estudiante in lista_estudiantes:
        print(f"{estudiante['nombre']} {estudiante['apellido']} -  Promedio: {estudiante['promedio']}")
        
# Función para buscar estudiante por nombre
def buscar_estudiante(lista_estudiantes):
    nombre_buscar = input("Ingrese el nombre del estudiante que desea buscar: ")
    for estudiante in lista_estudiantes:
        if estudiante['nombre'].lower() == nombre_buscar.lower():
            print(f"Estudiante encontrado: {estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")
            return
    print("Estudiante no encontrado.")
    
# Función para eliminar estudiante
def eliminar_estudiante(lista_estudiantes):
    nombre_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    for estudiante in lista_estudiantes:
        if estudiante['nombre'].lower() == nombre_eliminar.lower():
            lista_estudiantes.remove(estudiante)
            print(f"Estudiante {estudiante['nombre']} {estudiante['apellido']} dado de baja exitosamente.")
            return
    print("Estudiante no encontrado.")