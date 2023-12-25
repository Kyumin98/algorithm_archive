import sys
sys.setrecursionlimit(10**6)

_input = lambda : sys.stdin.readline()

N = int(_input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
result = []
def dfs(node):
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            result.append((i,node))
            dfs(i)

for i in range(N-1):
    start, end = list(map(int, _input().split()))
    graph[start].append(end)
    graph[end].append(start)

dfs(1)
result.sort(key=lambda x: x[0])
for item in result:
    print(item[1])
