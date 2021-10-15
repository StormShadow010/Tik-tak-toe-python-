#Impresion inicio
def impresioinicio(R):
        # For printing the matrix
        matrix = []
        for i in range(R):  # A for loop for row entries
            a = []
            for j in range(R):  # A for loop for column entries
                a.append(" * ")
            matrix.append(a)

        for i in range(R):
            for j in range(R):
                print(matrix[i][j], end=" ")
            print()
        return matrix