#Suma de matrices
""""Leer 2 matrices de 3 x 3 y sumar en una matriz"""

matriz1 = [
    [1, 2],
    [3, 4]
    [5, 6]
]

matriz2 = [
    [7, 8],
    [9, 10]
    [11, 12]
]

matriz3 = []
for i in range(len(matriz1)):
    matriz3.append([])
    for j in range(len(matriz1)):
        matriz3[i].append(matriz1[i][j] + matriz2[i][j])

print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("Matriz 2:")
for fila in matriz2:
    print(fila)

print("Matriz 3 (suma):")
for fila in matriz3:
    print(fila)





