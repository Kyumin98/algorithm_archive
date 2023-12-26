import sys

_input = lambda : sys.stdin.readline()

N, M, B = [* map(int, _input().split())]

graph = [list(map(int, input().split())) for _ in range(N)]
time_spent = (sys.maxsize, 0)
for height in range(257):
    curr_time_spent = 0
    blocks = B
    for i in range(N):
        for j in range(M):
            diff = graph[i][j] - height
            if diff == 0:
                continue
            elif diff < 0:
                curr_time_spent += abs(diff) * 1
                blocks -= 1 * abs(diff)
            else:
                curr_time_spent += abs(diff) * 2
                blocks += 1 * abs(diff)

    if blocks < 0:
        flag = False
    else:
        flag = True
    if flag and time_spent[0] >= curr_time_spent:
        time_spent = (curr_time_spent, height)
print(str(time_spent[0]) + " " + str(time_spent[1]))
