import sys

_input = lambda : sys.stdin.readline()

N = int(_input())

graph= [[]]
for _ in range(N):
    graph.append(list(map(int, _input().replace("\n", ""))))
visited = [[False for _ in range(N+1) if h != 0] for h in range(N + 1)]
dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]
def dfs(y, x):
    global cnt
    if graph[y][x] == 0 or visited[y][x] == True:
        return

    visited[y][x] = True

    for i in range(4):
        ch_x = x + dx[i]
        ch_y = y + dy[i]
        if 0 <= ch_x < N and 1 <= ch_y <= N:
            if not visited[ch_y][ch_x]:
                dfs(ch_y, ch_x)

    cnt += 1
result = []
for i in range(1, N+1):
    for j in range(N):
        cnt = 0
        dfs(i, j)
        if cnt > 0:
            result.append(cnt)

result.sort()
print(len(result))
[print(item) for item in result]
