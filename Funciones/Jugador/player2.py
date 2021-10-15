#Jugada del player
def jugada2(R,matriz):
    fila, columna = 10e10, 10e10
    jugada = False
    while jugada == False:
        while fila > R - 1:
            fila = int(input("Valor de la fila:"))
            if fila > R - 1:
                print("Valor fuera de rango, vuelva ingresar")
        while columna > R - 1:
            columna = int(input("Valor de la columna:"))
            if columna > R - 1:
                print("Valor fuera de rango, vuelva ingresar")
        if matriz[fila][columna] == " x " or matriz[fila][columna] == " 0 " :
            print("Posicion ya ocupada,ingresar de nuevo fila y columna.")
        else:
            matriz[fila][columna] = " x "
            jugada = True
        fila, columna =10e10, 10e10
    return matriz