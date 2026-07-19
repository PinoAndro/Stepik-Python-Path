n, m = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
step = 1
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            matrix[i][j] = step
            step += 1
            continue
        if m > n:
            if matrix[i][j] == 0:
                matrix[i][j] = step
                step += 1
                try:
                    for k in range(1, 1 + max(n, m) // min(n, m) +((j + 1) // min(n, m))):
                        matrix[i + k][j - k] = matrix[i][j] + k
                        step += 1
                except IndexError:
                    continue
        elif m == n:
            if matrix[i][j] == 0:
                matrix[i][j] = step
                step += 1
                try:
                    for k in range(1, i + j + 1):
                        matrix[i + k][j - k] = matrix[i][j] + k
                        step += 1
                except IndexError:
                    continue
        else:
            if matrix[i][j] == 0:
                matrix[i][j] = step
                step += 1
                try:
                    for k in range(1, 1 + min(n, m) // max(n, m) +((j + 1) // max(n, m))):
                        matrix[i + k][j - k] = matrix[i][j] + k
                        step += 1
                except IndexError:
                    continue

for row in matrix:
    print(*row)
