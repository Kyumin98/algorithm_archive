import sys

_input = lambda : sys.stdin.readline()

K = int(_input())
stack = []
for i in range(K):
    data = int(_input())
    if data != 0:
        stack.append(data)
    else:
        stack.pop()
_sum = 0
while stack:
    _sum += stack.pop()

print(_sum)
