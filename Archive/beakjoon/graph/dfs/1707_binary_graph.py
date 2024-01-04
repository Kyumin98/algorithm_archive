import sys
sys.setrecursionlimit(10**6)

_input = lambda : sys.stdin.readline()

def dfs(node):
    global result

    for item in graph[node]:
        if visited[item] == False:
            if visited[node] == 1:
                visited[item] = 2
            if visited[node] == 2:
                visited[item] = 1
            dfs(item)
        else:
            if visited[node] == visited[item]:
                result = False
                return

test_case = int(_input())

for loop in range(test_case):
    cnt = 0

    V, E = list(map(int, _input().split()))

    edges = [tuple(map(int, _input().split())) for _ in range(E)]

    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    result = True

    for i in range(E):
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])

    for i in range(1, V + 1):
        if visited[i] == False:
            visited[i] = 1
            dfs(i)
            if result == False:
                break

    if result == False:
        print("NO")
    else:
        print("YES")
