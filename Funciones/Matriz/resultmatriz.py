#Impresion de la matriz nueva con los cambios en las jugadas
def impresionnueva(R,matriz):
    for i in range(R):
        for j in range(R):
            print(matriz[i][j], end=" ")
        print()