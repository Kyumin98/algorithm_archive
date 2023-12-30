import sys, copy
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
total_area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def recursion(_list, x, y):
    if not _list[x][y]:
        return
    _list[x][y] = False
    if x-1 >= 0:
        recursion(_list, x-1, y)
    if y+1 < len(_list):
        recursion(_list, x, y+1)
    if x + 1 < len(_list):
        recursion(_list, x + 1, y)
    if y - 1 >= 0:
        recursion(_list, x, y - 1)

max = 0

for rain in range(0, 101, 1):
    cnt = 0
    total_area_tmp = copy.deepcopy(total_area)
    for i in range(N):
        for j in range(N):
            if total_area_tmp[i][j] <= rain:
                total_area_tmp[i][j] = False
            else:
                total_area_tmp[i][j] = True

    for i in range(N):
        for j in range(N):
            if total_area_tmp[i][j]:
                recursion(total_area_tmp, i, j)
                cnt += 1
    if max < cnt:
        max = cnt

print(max)
