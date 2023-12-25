import sys

_input = lambda: sys.stdin.readline()

N = int(_input())
matrix = [* map(int, _input().split())]
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if matrix[i] > matrix[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
