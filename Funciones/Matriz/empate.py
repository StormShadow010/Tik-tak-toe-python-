def buscarempate(R,matriz,empate):
    ganado = False
    em=0
    for i in range(R):
        for j in range(R):
            if matriz[i][j]==" 0 " or matriz[i][j]==" x ":
                em+=1
                if em==9:
                    empate+=1
                    print("Empate,nadie gano")
                    ganado=True
                    break
    return ganado,empate