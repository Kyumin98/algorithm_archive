import sys

_input = lambda : sys.stdin.readline()

N, M = [* map(int, _input().split())]

lower_stone = [int(_input()) for _ in range(M)]

dp = [[sys.maxsize]*(int((2*N)**0.5)+2) for _ in range(N+1)]

dp[1][0] = 0
for i in range(2, N+1):
    if i in lower_stone:
        continue
    for jump in range(1, int((2*i)**0.5)+1):
        dp[i][jump] = min(dp[i-jump][jump-1], dp[i-jump][jump], dp[i-jump][jump+1]) + 1

print(min(dp[N]))
