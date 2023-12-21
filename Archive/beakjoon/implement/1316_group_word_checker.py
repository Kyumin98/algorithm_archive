import sys

_input = lambda : sys.stdin.readline()

N = int(_input())
cnt = 0
for i in range(N):
    line = _input().replace("\n", "")
    stack = []
    for j in range(len(line)):
        if line[j] not in stack or stack[-1] == line[j]:
            stack.append(line[j])
        else:
            break
    if len(stack) == len(line):
        cnt += 1
print(cnt)
