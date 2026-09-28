matriz = []
for i in range(2):
    matriz.append([])
    for j in range(2):
        matriz[i].append(int(input(f"ingrese el valor de la posicion [{i}][{j}]: ")))

#Mostrar la matriz
print("La matriz ingresada de 2x2 es de:")
for fila in matriz:
    print(fila)
