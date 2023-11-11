import sys, heapq

_input = lambda: sys.stdin.readline()

N = int(_input())
heap = []
for _ in range(N):
    x = int(_input())
    if x != 0:
        heapq.heappush(heap, (-x, x))
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
