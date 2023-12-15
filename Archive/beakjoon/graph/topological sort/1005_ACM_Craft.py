import sys
from collections import deque

def bfs(queue, inedge, timerecord):
    while(queue):
        v = queue.popleft()
        time = timerecord[v]
        for nv in graph[v]:
            inedge[nv] = inedge[nv] - 1
            if inedge[nv] == 0:
                queue.append(nv)
            timerecord[nv] = max(timerecord[nv], time + timelist[nv])

    print(timerecord[w])

test = int(sys.stdin.readline())
for t in range(test):
    n, k = list(map(int, sys.stdin.readline().split()))
    timelist = [-1] + list(map(int, sys.stdin.readline().split()))
    graph = {}
    inedge = {}
    for i in range(1, n+1):
        graph[i] = []
        inedge[i] = 0
    for i in range(k):
        x, y = list(map(int, sys.stdin.readline().split()))
        graph[x].append(y)
        inedge[y] +=1
    w = int(sys.stdin.readline())

    queue = deque()
    timerecord = [-1] + [0 for x in range(1, n+1)]
    for i in range(1, n+1):
        if inedge[i] == 0:
            queue.append(i)
            timerecord[i] = timelist[i]
    bfs(queue, inedge, timerecord)
