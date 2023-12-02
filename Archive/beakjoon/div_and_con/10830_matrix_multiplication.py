import sys

inputs = list(map(int, sys.stdin.readline().split()))
N, B = inputs[0], inputs[1]
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def matrix_multiple(matrix, N, B):

    def multiple(matrix, N):
        result = []
        for loop in range(N):
            row = []
            for i in range(N):
                val = 0
                for j in range(N):
                    val += matrix[loop][j] * matrix[j][i]
                row.append(val)
            result.append(row)

        return result

    def rtn_remain(matrix, N):
        result = []
        for i in range(N):
            row = []
            for j in range(N):
                row.append(matrix[i][j] % 1000)
            result.append(row)

        return result

    if B == 1:
        return rtn_remain(matrix, N)

    val = matrix_multiple(matrix, N, B//2)

    if B % 2 == 0:
        return rtn_remain(multiple(val, N), N)
    else:
        val = multiple(val, N)
        result = []
        for loop in range(N):
            row = []
            for i in range(N):
                mat = 0
                for j in range(N):
                    mat += val[loop][j] * matrix[j][i]
                row.append(mat)
            result.append(row)
        return rtn_remain(result, N)

ans = matrix_multiple(matrix, N, B)
for i in range(len(ans)):
    for j in range(len(ans)):
        if j == len(ans)-1:
            print(ans[i][j], end='')
        else:
            print(ans[i][j], end=' ')
    print()
