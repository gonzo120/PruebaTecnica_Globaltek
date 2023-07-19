# Inicializar las listas de productos y existencias
dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
dairy_stock = [28, 36, 50]
cleaning_products = []
cleaning_stock = []
grain_products = []
grain_stock = []

# Función para agregar un producto al inventario
def agregar_producto(nombre, cantidad, grupo):
    if grupo == "dairy":
        if nombre in dairy_products:
            indice = dairy_products.index(nombre)
            dairy_stock[indice] += cantidad
        else:
            dairy_products.append(nombre)
            dairy_stock.append(cantidad)
    elif grupo == "cleaning":
        if nombre in cleaning_products:
            indice = cleaning_products.index(nombre)
            cleaning_stock[indice] += cantidad
        else:
            cleaning_products.append(nombre)
            cleaning_stock.append(cantidad)
    elif grupo == "grain":
        if nombre in grain_products:
            indice = grain_products.index(nombre)
            grain_stock[indice] += cantidad
        else:
            grain_products.append(nombre)
            grain_stock.append(cantidad)

# Función para mostrar el reporte de inventario
def ver_reporte():
    print("Nombre                         Existencias")
    print("---------------------------------------")
    for i in range(len(dairy_products)):
        print("{:<30} {:>10}".format(dairy_products[i], dairy_stock[i]))
    for i in range(len(cleaning_products)):
        print("{:<30} {:>10}".format(cleaning_products[i], cleaning_stock[i]))
    for i in range(len(grain_products)):
        print("{:<30} {:>10}".format(grain_products[i], grain_stock[i]))
    print("---------------------------------------")

# Menú principal del programa
while True:
    print("Sistema de inventario. Ingrese una opcion:")
    print("-----------------------------------------------")
    print("1. Agregar producto")
    print("2. Ver reporte de inventario")
    print("3. Salir")
    opcion = input("Su opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        grupo = input("Ingrese el grupo (dairy, cleaning, grain): ")
        agregar_producto(nombre, cantidad, grupo)
    elif opcion == "2":
        ver_reporte()
    elif opcion == "3":
        break
