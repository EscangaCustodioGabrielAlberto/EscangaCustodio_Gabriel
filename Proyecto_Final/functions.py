# Función para mostrar las opciones del menu
def mostrar_menu():
    print("Abarrotes 'Raccon City'")
    print("Sistema de Gestión de Productos")
    print("1. Agregar un producto")
    print("2. Mostrar lista completa de productos")
    print("3. Buscar producto por nombre")
    print("4. Buscar producto por ID")
    print("5. Eliminar producto")
    print("6. Editar producto")
    print("7. Salir")


# Función para agregar un producto
def agregar_producto(lista_productos):
    nombre = input("Ingrese el nombre del producto: ")
    for producto in lista_productos:
        if producto['nombre'].lower() == nombre.lower():
            print("Producto ya registrado")
            return
    id = input("Ingrese el ID del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible del producto: "))
    categoria = input("Ingrese la categoria del producto: ")

    lista_productos.append({"nombre": nombre, "ID": id, "precio": precio, "cantidad": cantidad, "categoria": categoria})
    
    print(f"El producto '{nombre}' con ID:{id} fue agregado exitosamente.")

# Función para mostrar lista de productos
def mostrar_productos(lista_productos):
    if not lista_productos:
        print("No hay productos en la lista")
        return
    print("Lista de productos")
    for producto in lista_productos:
        print(f"{producto['nombre']} - ID:{producto['ID']} - Precio: {producto['precio']} - Cantidad disponible:{producto['cantidad']} - Categoria:{producto['categoria']}") 
        
# Función para buscar productos por nombre
def buscar_producto(lista_productos):
    if not lista_productos:
        print("No hay productos en la lista")
        return
    nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")
    for producto in lista_productos:
        if producto['nombre'].lower() == nombre_buscar.lower():
            print(f"Producto encontrado: {producto['nombre']} - ID:{producto['ID']} - Precio: {producto['precio']} - Cantidad disponible:{producto['cantidad']} - Categoria:{producto['categoria']}")
            return
    print("Producto no encontrado.")

# Funcion para buscar productos por medio de su ID
def buscar_producto_id(lista_productos):
    if not lista_productos:
        print("No hay productos en la lista")
        return
    id_buscar = input("Ingrese el ID del producto que desea buscar: ")
    for producto in lista_productos:
        if producto['ID'].lower() == id_buscar.lower():
            print(f"Producto encontrado: {producto['nombre']} - ID:{producto['ID']} - Precio: {producto['precio']} - Cantidad disponible:{producto['cantidad']} - Categoria:{producto['categoria']}")
            return
    print("Estudiante no encontrado.")
    
# Función para eliminar productos
def eliminar_producto(lista_productos):
    if not lista_productos:
        print("No hay productos en la lista")
        return
    nombre_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
    for producto in lista_productos:
        if producto['nombre'].lower() == nombre_eliminar.lower():
            respuesta = input("Seguro que deseas eliminar este elemento? (Y/N)")
            if (respuesta.lower() == "y"):
                print("Se removera el producto...")
            elif (respuesta.lower() == "n"):
                print("No se elimino el producto. Regresando al menu principal.")
                return
            else:
                print("Respuesta no valida")
                return
            lista_productos.remove(producto)
            print(f"Producto '{producto['nombre']}' con ID:{producto['ID']} Eliminado exitosamente")
            return
    print("preoducto no encontrado.")

# Funcion para editar productos
def editar_producto(lista_productos):
    if not lista_productos:
        print("No hay productos en la lista")
        return
    print("Lista de productos disponibles.")
    for producto in lista_productos:
        print(f"-{producto['nombre']}") 
    producto_a_editar = input("Que producto deseas editar?: ")
    for producto in lista_productos:
        if producto['nombre'].lower() == producto_a_editar.lower():
            print(f"Producto '{producto['nombre']}' selecionado.")
            print("Seguro que quieres editar este producto? (Y/N)")
            respuesta = input("R=")
            if (respuesta.lower() == "n"):
                print("Se cancelo la edicion del producto.")
                return
            elif (respuesta.lower() == "y"):
                print("Mostrando datos para editar") 
            else:
                print("Opcion no valida")
                return
            print("-----------------------------")
            for clave, valor in producto.items():
                print(f"{clave}: {valor}")
            valor_a_editar = input("Que valor deseas editar")
            if (valor_a_editar.lower() == "nombre"):
                nuevo_nombre = input("Ingresa el nuevo nombre del producto: ")
                producto["nombre"] = nuevo_nombre
                print("Nombre editado correctamente")
            elif (valor_a_editar.lower() == "ID"):
                nuevo_id = input("Ingresa el nuevo ID del producto: ")
                producto["ID"] = nuevo_id
                print("ID editado correctamente")
            elif (valor_a_editar.lower() == "precio"):
                nuevo_precio = input("Ingresa el nuevo precio del producto: ")
                producto["precio"] = nuevo_precio
                print("Precio editado correctamente")
            elif (valor_a_editar.lower() == "cantidad"):
                nueva_cantidad = input("Ingresa la cantidad actual disponible del producto: ")
                producto["cantidad"] = nueva_cantidad
                print("Cantidad editada correctamente")
            elif (valor_a_editar.lower() == "categoria"):
                nueva_categoria = input("Ingresa la nueva categoria del producto: ")
                producto["categoria"] = nueva_categoria
                print("Categoria editada correctamente")
            else:
                print("Valor para editar no disponible.")
            
