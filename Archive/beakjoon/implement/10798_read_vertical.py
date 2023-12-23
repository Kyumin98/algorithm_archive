import sys

_input = lambda : sys.stdin.readline()

matrix = []
for i in range(5):
    line = list(_input().replace("\n", ""))
    while len(line) < 15:
        line.append(" ")
    matrix.append(line)
for low in range(15):
    for item in range(5):
        if matrix[item][low] == " ":
            continue
        print(matrix[item][low], end='')
