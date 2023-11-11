import sys
from collections import deque

_input = lambda : sys.stdin.readline()

size, virus = [* map(int, _input().split())]
visited = [[False for _ in range(size+1) if h != 0] for h in range(size + 1)]
graph= [[]]
for _ in range(size):
    graph.append(list(map(int, _input().split())))

S, Y, X = [* map(int, _input().split())]
dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]

_deque = deque()
v_list = []
for i in range(1, size+1):
    for j in range(size):
        if graph[i][j] != 0:
            v_list.append((graph[i][j], j, i))
v_list.sort(key=lambda x: x[0])

for _ in v_list:
    _deque.append(_)
loop = 0
while True:
    if loop == S:
        print(graph[Y][X-1])
        break
    for _ in range(len(_deque)):
        virus_number, x, y = _deque.popleft()

        for i in range(4):
            ch_x = x + dx[i]
            ch_y = y + dy[i]
            if 0 <= ch_x < size and 1 <= ch_y <= size:
                if graph[ch_y][ch_x] == 0:
                    graph[ch_y][ch_x] = virus_number
                    _deque.append((virus_number, ch_x, ch_y))

    loop += 1