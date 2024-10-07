import os  # Importa la librería os para manejar archivos.

# Inicializa la lista de productos, que contendrá diccionarios con nombre, precio y cantidad.
productos = []

# Función para cargar los productos desde el archivo al iniciar el programa.
def cargar_datos():
    # Verifica si el archivo productos.txt existe antes de intentar cargar los datos.
    if os.path.exists("productos.txt"):
        # Abre el archivo en modo lectura.
        with open("productos.txt", "r") as file:
            # Recorre cada línea del archivo.
            for linea in file:
                # Divide la línea en nombre, precio y cantidad, separando por coma.
                nombre, precio, cantidad = linea.strip().split(", ")
                # Convierte el precio a float y la cantidad a int, luego añadimos el producto a la lista.
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
    else:
        # Si no existe el archivo, mostramos un mensaje y continuamos con una lista vacía.
        print("No se encontró el archivo productos.txt. Comenzando con una lista vacía.")

# Función para guardar los productos en un archivo de texto.
def guardar_datos():
    # Abre el archivo en modo escritura, esto sobrescribirá el archivo existente.
    with open("productos.txt", "w") as file:
        # Recorre la lista de productos.
        for producto in productos:
            # Escribe cada producto en una línea en formato: nombre, precio, cantidad.
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")
    # Mensaje que indica que los datos fueron guardados exitosamente.
    print("Datos guardados correctamente.")

# Función para añadir un producto nuevo a la lista.
def añadir_producto():
    # Pedimos el nombre del producto al usuario.
    nombre = input("Introduce el nombre del producto: ")
    
    # Ciclo para asegurar de que el usuario introduzca un precio válido (número flotante).
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break  # Sale del bucle si se introduce un número válido.
        except ValueError:
            print("El precio debe ser un número válido.")  # Muestra un mensaje de error si el valor no es un número.

    # Ciclo para asegurar de que el usuario introduzca una cantidad válida (número entero).
    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break  # Sale del bucle si se introduce un número válido.
        except ValueError:
            print("La cantidad debe ser un número entero válido.")  # Muestra un mensaje de error si el valor no es válido.

    # Añade el producto como un diccionario a la lista de productos.
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    # Confirmar que el producto ha sido añadido.
    print(f"Producto '{nombre}' añadido correctamente.")

# Función para ver todos los productos almacenados.
def ver_productos():
    # Si hay productos en la lista, mostrar.
    if productos:
        # Enumera cada producto para mostrar su número, nombre, precio y cantidad.
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        # Si no hay productos, mostrar un mensaje.
        print("No hay productos en la lista.")

# Función para actualizar los detalles de un producto existente.
def actualizar_producto():
    # Primero mostrar los productos disponibles para que el usuario elija cuál actualizar.
    ver_productos()
    # Si hay productos, continuar con la actualización.
    if productos:
        # Pedir al usuario el nombre del producto que desea actualizar.
        nombre = input("Introduce el nombre del producto que deseas actualizar: ")
        
        # Recorre la lista de productos buscando el producto con ese nombre.
        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():  # Ignorar mayúsculas y minúsculas.
                print("Producto encontrado. Ingresa los nuevos valores (o presiona Enter para mantener el valor actual).")
                # Permitir que el usuario deje un campo vacío para no cambiarlo.
                nuevo_nombre = input(f"Nombre actual ({producto['nombre']}): ") or producto["nombre"]
                
                # Actualizar el precio si el usuario introduce un valor válido, de lo contrario, se mantiene el actual.
                try:
                    nuevo_precio = float(input(f"Precio actual ({producto['precio']}): ") or producto["precio"])
                except ValueError:
                    print("Precio no válido. No se actualizará.")
                    nuevo_precio = producto["precio"]

                # Actualizar la cantidad si el usuario introduce un valor válido, de lo contrario, se mantiene la actual.
                try:
                    nueva_cantidad = int(input(f"Cantidad actual ({producto['cantidad']}): ") or producto["cantidad"])
                except ValueError:
                    print("Cantidad no válida. No se actualizará.")
                    nueva_cantidad = producto["cantidad"]

                # Actualiza los valores del producto.
                producto["nombre"] = nuevo_nombre
                producto["precio"] = nuevo_precio
                producto["cantidad"] = nueva_cantidad
                print(f"Producto '{nuevo_nombre}' actualizado correctamente.")
                break  # Sale del bucle una vez actualizado el producto.
        else:
            # Si no se encuentra el producto, mostrar un mensaje.
            print("Producto no encontrado.")

# Función para eliminar un producto de la lista.
def eliminar_producto():
    # Mostrar los productos disponibles.
    ver_productos()
    # Si hay productos, continuar con la eliminación.
    if productos:
        # Pedir el nombre del producto que se desea eliminar.
        nombre = input("Introduce el nombre del producto que deseas eliminar: ")
        
        # Recorre la lista de productos buscando el producto a eliminar.
        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():  # Ignora mayúsculas y minúsculas.
                productos.remove(producto)  # Elimina el producto de la lista.
                print(f"Producto '{nombre}' eliminado correctamente.")
                break
        else:
            # Si no se encuentra el producto, mostrar un mensaje.
            print("Producto no encontrado.")

# Función principal que gestiona el menú del sistema.
def menu():
    cargar_datos()  # Cargar productos desde el archivo al inicio del programa.

    while True:
        # Mostrar las opciones del menú.
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        # Pedir al usuario que elija una opción.
        opcion = input("Selecciona una opción: ")

        # Ejecutar la función correspondiente según la opción elegida.
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()  # Guardar los datos antes de salir.
            print("Saliendo del sistema.")
            break  # Termina el ciclo y sale del programa.
        else:
            # Si la opción es inválida, mostrar un mensaje de error.
            print("Por favor, selecciona una opción válida.")

# Iniciar el programa llamando a la función menú.
menu()