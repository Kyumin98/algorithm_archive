import sys

_input = lambda: sys.stdin.readline()

N = int(_input())
cnt = 2
while N != 1:
    if N % cnt == 0:
        N = N // cnt
        print(cnt)
        cnt = 2
    else:
        cnt += 1
