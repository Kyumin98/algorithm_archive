import sys

_input = lambda : sys.stdin.readline()

N = int(_input())
_list = [* map(int, _input().split())]
dp = [[0]*N for i in range(N)]

for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    if _list[i] == _list[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0
for i in range(N-2):
    for j in range(N-i-2):
        k = i + j + 2
        if _list[j] == _list[k] and dp[j+1][k-1] == 1:
            dp[j][k] = 1
M = int(_input())
for i in range(M):
    y, x = [* map(int, _input().split())]
    print(dp[y-1][x-1])
