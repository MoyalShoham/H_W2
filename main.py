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




#ex 1:
def decRows(matrix, scalar, index, less):
       for i in range(0, len(matrix)):
             matrix[less][i] -= scalar*matrix[index][i]
       return matrix


def gausElimination(matrix, B):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == j and matrix[i][j] is not 0:
                for k in range(i+1,len(matrix)):
                    scalar=0
                    if matrix[k][j]==0:continue
                    else:
                        scalar = matrix[k][j]/matrix[i][j]
                    if scalar is not 0:
                        matrix = decRows(matrix, scalar, i, k)
                        B[k] -= scalar*B[i]
    return matrix


def results(matrix, B):
    x = [0, 0, 0]
    x[2] = B[2]/matrix[2][2]#solve the third
    x[1] = (B[1]-matrix[1][2]*x[2])/matrix[1][1]#solve the second using the third result
    x[0] = (B[0]-matrix[0][1]*x[1]-matrix[0][2]*x[2])/matrix[0][0]#solve the first using all the result
    return x



I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#matrix = [[1, 2, 1], [2, 6, 1], [1, 1, 4]]
matrix = [[-1.41, 2, 0], [0, 2, -1.41], [1, -1.41, 1]]
# matrix = [[-1.41, 2, 0], [0, 2, -1.41], [0, 0, 1.01]]

B = [1, 1, 1]
for i in matrix:
         print(i)

print()
matrix = gausElimination(matrix,B)
for i in matrix:
         print(i)

print("result")
print(B)
print()
print(results(matrix, B))
