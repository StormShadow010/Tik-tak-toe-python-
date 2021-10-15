def ganaplayer(R,matriz,gu,gpc,em):
    rayajug = 0
    ganado = False
    # Filas
    for fi in range(0, R, 1):
        i = fi
        for j in range(0, R, 1):
            if matriz[i][j] == " 0 ":
                rayajug += 1
                if rayajug == R:
                    rayajug = 0
                    print("Le ganaste a la maquina, maestro")
                    gu = gu + 1
                    ganado = True
                    break
        rayajug = 0
    # Columnas
    for fi in range(0, R, 1):
        i = fi
        for j in range(0, R, 1):
            if matriz[j][i] == " 0 ":
                rayajug += 1
                if rayajug == R:
                    rayajug = 0
                    print("Le ganaste a la maquina, maestro")
                    gu = gu + 1
                    ganado = True
                    break
        rayajug = 0
    #Diagonales
    #Diagonales iguales
    for i in range(R):
        for j in range(R):
            if i==j:
                if matriz[i][j]==" 0 ":
                    rayajug += 1
                    if rayajug == R:
                        rayajug = 0
                        print("Le ganaste a la maquina, maestro")
                        gu = gu + 1
                        ganado = True
                        break
    rayajug = 0
    #Diagonales secundarias
    for i in range(R):
        for j in range(R):
            if i+j==R-1:
                if matriz[i][j]==" 0 ":
                    rayajug += 1
                    if rayajug == R:
                        rayajug = 0
                        print("Le ganaste a la maquina, maestro")
                        gu = gu + 1
                        ganado = True
                        break
    rayajug = 0

    return ganado, gu, gpc, em