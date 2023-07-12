## PROYECTO #1 - CAJA REGISTRADORA (PARA TIENDA DE COMESTIBLES):

print("BIENVENIDO A LA CAJA REGISTRADORA GSPro \n")

# ENTRADA DE PRODUCTOS (PARA LOS EMPLEADOS) / STOCK DE LA TIENDA
print("EMPLEADO, ingresa el inventario de productos a vender (uso autorizado para empleados)")

articulos = {}  # Iniciamos definiendo un dicc. que almacenará: {producto,precio,cantidad}

while True:
    producto = input("Ingresa el nombre del artículo (o ingresa 'salir' para terminar): \n")
    producto = producto.lower()

    if producto.lower() == "salir":
        break
    else:
        precio = float(input("Ingresa el precio del artículo (en $): "))
        cantidad = int(input("Ingresa la cantidad del artículo: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0") 
            cantidad = int(input("Cantidad: "))
            
    print("Cargado con éxito al sistema \n")
    
    articulos[producto] = {"precio": precio,"cantidad": cantidad}
    
# Aquí generamos el primer diccionario para realizar cálculos e iteraciones.
# Este es un diccionario que se genera asignando a cada clave [producto] un nuevo diccionario; de la siguiente manera:
# articulos = {'producto':{'precio':precio,'cantidad':cantidad}}

print("\n--- Lista de Artículos cargados al sistema ---\n")
for nombre,articulo in articulos.items():
    print("Nombre:", nombre)
    print("Precio:", articulo['precio'],"$")
    print("Cantidad:", articulo['cantidad'])
    print("------------------------")

while True:
    # PROCESAMIENTO DE COMPRA (CLIENTES):
    print("Procesamiento de compra \n")
    print("¡Bienvenido estimado cliente! \n --- A continuación te mostramos una lista de los productos disponibles en nuestra tienda: ---")

    for nombre,articulo in articulos.items():
        print("✓",nombre,articulo['precio'],"$")
        
    print("-------------------------")
    print("Por favor, ingrese los productos y la cantidad que desea comprar (uno por uno): \n")

    lista_compra = {} # Definimos un nuevo diccionario que permita almacenar los productos ingresados por el usuario
    while True:       # junto con su respectivo precio(vinculado con el dict "articulos")
        
        producto = input("Producto (o ingresa 'salir' para finalizar el pedido): \n")
        producto = producto.lower()
        if producto.lower() == "salir":
            break
        
        while producto not in articulos: 
        # Esta sentencia (not in) permite determinar si el valor de 'producto' se encuentra el el dicc. "articulos" 
            print("Lo sentimos, el producto ingresado no está disponible en nuestra tienda")
            producto = input("Ingresa otro producto (o ingresa 'salir' para finalizar el pedido): ")
            if producto in articulos:
                break
    
        cantidad = int(input("Cantidad: "))
                
        while cantidad <= 0:
            print("La cantidad debe ser mayor a 0") 
            cantidad = int(input("Cantidad: "))
            if cantidad >= 0:
                break

        while cantidad > articulos[producto]['cantidad']:
            print("Lo sentimos, no tenemos suficiente stock de este producto")
            cantidad = int(input("Ingresa una cantidad menor: "))
            if cantidad <= articulos[producto]['cantidad']:
                break
        
        lista_compra[producto] = {"precio":articulos[producto]['precio'],"cantidad":cantidad}
        # Generamos el 2do dicc. que nos permitirá realizar el cálculo toal de la compra.
        
    # CÁLCULO DE LA COMPRA

    total = 0
    suma = 0
    for producto in lista_compra.values():
        total += producto['precio'] * producto['cantidad']
        suma += producto['cantidad']

    # LISTA DE PRODUCTOS COMPRADOS Y TOTAL DE LA COMPRA

    print("\n PEDIDO TOTAL:" )
    for i,j in lista_compra.items():
        print("✓",i,j['cantidad']) 
        
    print("-----------------------------------------------------------")
    print("")
    print("  \________","     ","CANTIDAD DE PRODUCTOS COMPRADOS:")
    print("   \       |","                ",suma)
    print("    \______|","      ","MONTO TOTAL DE LA COMPRA")
    print("     O     O","               ",total,"$")
    print("")
    print("-----------------------------------------------------------")
    
    salir = input("¿Desea procesar otra transacción? (ingrese 'si' o 'no'): ")
    if salir.lower() == "no":
        print("MUCHAS GRACIAS POR SU COMPRA, VUELVA PRONTO")
        break
    
      