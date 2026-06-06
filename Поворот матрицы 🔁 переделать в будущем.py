def abc(n):
    i = 0
    for j in range(n - 1):
        if j == 0:
            matrix[i][j], matrix[n - 1 - j][i] =  matrix[n - 1 - j][i], matrix[i][j]
            matrix[n - 1 - j][i], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[n - 1 - j][i]
            matrix[n - 1 - j][n - 1 - j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[n - 1 - j][n - 1 - j]
        else:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[j][i], matrix[j][n - 1 - j] = matrix[j][n - 1 - j], matrix[j][i]
            matrix[j][i], matrix[j][n - 1 - j] = matrix[j][n - 1 - j], matrix[j][i]
        return matrix
