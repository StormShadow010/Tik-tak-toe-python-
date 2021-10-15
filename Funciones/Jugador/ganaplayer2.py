def ganaplayer2(R, matriz, gu, gpc, em,name):
    rayamaquina = 0
    ganado = False
    # Filas
    for fi in range(0, R, 1):
        i = fi
        for j in range(0, R, 1):
            if matriz[i][j] == " x ":
                rayamaquina += 1
                if rayamaquina == R:
                    rayamaquina = 0
                    print(f"Gano {name}")
                    gpc = gpc + 1
                    ganado = True
                    break
        rayamaquina = 0
    # Columnas
    for fi in range(0, R, 1):
        i = fi
        for j in range(0, R, 1):
            if matriz[j][i] == " x ":
                rayamaquina += 1
                if rayamaquina == R:
                    rayamaquina = 0
                    print(f"Gano {name}")
                    gpc = gpc + 1
                    ganado = True
                    break
        rayamaquina = 0
    # Diagonales
    # Diagonales iguales
    for i in range(R):
        for j in range(R):
            if i == j:
                if matriz[i][j] == " x ":
                    rayamaquina += 1
                    if rayamaquina == R:
                        rayamaquina = 0
                        print(f"Gano {name}")
                        gpc = gpc + 1
                        ganado = True
                        break
    rayamaquina = 0
    # Diagonales secundarias
    for i in range(R):
        for j in range(R):
            if i + j == R - 1:
                if matriz[i][j] == " x ":
                    rayamaquina += 1
                    if rayamaquina == R:
                        rayamaquina = 0
                        print(f"Gano {name}")
                        gpc =gpc + 1
                        ganado = True
                        break
    rayamaquina = 0

    return ganado, gu, gpc, em