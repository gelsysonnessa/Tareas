# Módulo de Álgebra

# 1. Función para multiplicar matrices:
def multiplicacion_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if columnas_matriz1 != filas_matriz2:
        return "No es posible multiplicar las matrices. La cantidad de columnas de la Matriz 1 debe ser igual a la cantidad de filas de la matriz 2"    
    
    matriz_resultado = []

    for i in range(filas_matriz1):
        fila_resultado = []
        for j in range(columnas_matriz2):
            suma = 0
            for k in range(filas_matriz2):
                suma += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(suma)
        matriz_resultado.append(fila_resultado)

    return matriz_resultado

matriz1 = [[1,2],[3,4],[3,4]]
matriz2 = [[1,2],[3,4]]

print(multiplicacion_matrices(matriz1,matriz2))


# 3. Función para el producto vectorial:
def producto_vectorial(v1, v2):
    resultado = [0, 0, 0]
    resultado[0] = v1[1] * v2[2] - v1[2] * v2[1] # cada operación se sustituye en la posición 
    resultado[1] = v1[2] * v2[0] - v1[0] * v2[2] # correspondiente en el vector 'resultado' 
    resultado[2] = v1[0] * v2[1] - v1[1] * v2[0]
    return resultado

a = [1, 2, 3]
b = [4, 5, 6]
resultado = producto_vectorial(a, b)
print(resultado)


