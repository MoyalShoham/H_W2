# A = [[1, 2, 1], [2, 6, 1], [1, 1, 4]]
# matrixSize = 3
A = [[1, 2, 1, 3], [2, 6, 1, 4], [1, 1, 4, 7], [5, 4, 3, 1]]
matrixSize = 4

def multiplyMatrix(matrix1, matrix2):
    # result = [[0, 0, 0],
    #           [0, 0, 0],
    #           [0, 0, 0]]
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def LUsplit(matrix):
    # L = [[1, 0, 0],
    #      [0, 1, 0],
    #      [0, 0, 1]]
    L = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]

    x = 0
    y = 0
    size = 1
    i = 0
    newMatrix = matrix
    while size is not matrixSize:
        for k in range(len(matrix) - size):
            for j in range(len(matrix) - size):
                # U = [[1, 0, 0],
                #      [0, 1, 0],
                #      [0, 0, 1]]
                U = [[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]]
                pivot = newMatrix[x][y]
                U[j + size][i] = -1 * (newMatrix[j + size][i] / pivot)
                L[j + size][i] = (newMatrix[j + size][i] / pivot)
                newMatrix = multiplyMatrix(U, newMatrix)
            size = size + 1
            x = x + 1
            y = y + 1
            i = i + 1
        for r in L:
            print(r)
        print()
        for r in newMatrix:
            print(r)
        print()
        m = multiplyMatrix(L, newMatrix)
        for r in m:
            print(r)
        print()


result = LUsplit(A)