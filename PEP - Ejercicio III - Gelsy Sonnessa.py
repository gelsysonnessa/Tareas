# EJERCICIO III - PARCIAL I

n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))

matriz = []
numero = 0
for i in range(n): 
    filas = [] # --> defino la lista por la que estará compuesta la matriz
    for j in range(m): 
        if i % 2 == 0: # --> este condicional evalúa si i es un número PAR
            numero += 1  # Acumulador para agregar la secuencia 1,2,3...n
            filas.append(numero)
        else:
            numero += 1
            filas.append(numero)
            filas.sort(reverse=True) # --> esta función permite invertir la lista de forma ascendente a descendente.
            # de esta forma se genera el zig zag.
                                            
    matriz.append(filas)

for fila in matriz:
    for numeros in fila:
        print("\t", numeros, end = "")
    print()

# NOTA: Use "\t" alinear rápidamente los valores en columna. 
#       El end=" " sirve para que el print no cambie de linea luego de imprimir un valor.
#       Cuando se ha impreso toda una linea, se coloca ootro print() para forzar una nueva línea.