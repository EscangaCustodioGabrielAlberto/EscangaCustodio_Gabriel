# E n python existen los siguientes modos de lectura y escritura de archivos:
# 'r': Modo de lectura (read) -> Abre un archivo para leerlo. el archivo debe eistir, si no existe el programa nos marcara un error.
# 'w': Modo de escritura (write) -> Abre un archivo para escribir en el. si el archivo ya existe, se sobrescribe. si no existe, se crea uno nuevo.
# 'a': Modo de anexado (append) -> Abre un archivo para agregar contenido al final del mismo. si el archivo no existe se crea uno nuevo.
# 'r+': Modo de lectura y escritura -> Abre un archivo para leer y escribir. si el archivo no existe se marcara error.
# 'w+': Modo de escritura y lectura -> Abre un archivo para escribir y leer, si el archivo no existe, se crea uno nuevo, sobrescribe el archivo si ya existe.
# 'a+': Modo de anexado y lectura -> Abre un archivo para agregar contenido al final y leerlo. si el archivo no existe, se crea uno nuevo.

#Apertura de archivo
# open("ruta/archivo.txt", modo)

#Cerrar el archivo
# archivo.close()

# Podemos abrir el archivo haciendo uso de 'with', el cual cierra el archivo de manera automatica al finalizar el bloque de codigo

# with open("ruta/archivo.txt", modo) as archivo:
#   # Operaciones con el archivo

# with open("ManejoArchivos/archivo.txt", "r") as archix:
#     contenido = archix.read() #Leer todo el contenido del archivo y lo va a almacenar
# print(contenido)

# with open("archivo.txt", "r") as f:
#     for linea in f: #lee el archico linea por linea
#         print(linea.strip()) # Imprimir cada linea sin espacios adicionales

# with open("archivo.txt", "w") as f:
#     f.write("Esta line ahora fue reemplazada")
#     f.write("MUAJAJAJAJAJAJAJAJA")

# with open("archivo.txt", "a") as archix:
#     archix.write("Esta linea se añadio al final del archivo")

# with open("archivo.txt", "r+") as f:
#     f.write("se añadio usando r+")

# with open("archivo.txt", "w+") as f:
#     f.write("Escrito con w+")
#     f.seek(0) #Para volver al inicio del archivo para leer lo que se escribio
#     contenido = f.read()
#     print(contenido)

with open("archivo2.txt", "a+") as f:
    f.write("Escribiendo archivo2 usando w+")
    f.seek(0) #Para volver al inicio del archivo para leer lo que se escribio
    contenido = f.read()
    print(contenido)
