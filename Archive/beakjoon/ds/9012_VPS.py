import sys

_input = lambda : sys.stdin.readline()

N = int(_input())

for i in range(N):
    data = _input().replace("\n", "")
    stack = []

    _list = list(data)

    for item in _list:
        if item == "(":
            stack.append(item)
        elif item == ")":
            if stack:
                stack.pop()
            else:
                stack.append(item)
                break
    if stack:
        print("NO")
    else:
        print("YES")
