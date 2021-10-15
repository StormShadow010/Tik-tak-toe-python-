import random
#Jugada maquina
def computador(R,matriz):
    correct=False
    while correct==False:
        fila = random.randint(0, R-1)
        columna = random.randint(0, R-1)
        if matriz[fila][columna]==" * ":
            matriz[fila][columna]=" x "
            correct=True

    return matriz