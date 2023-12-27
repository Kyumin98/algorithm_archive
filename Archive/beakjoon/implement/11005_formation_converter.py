import sys

_input = lambda : sys.stdin.readline()

N, B = [* map(int, _input().split())]

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
loop = 1
result = ""
while N % (B ** loop) != N:
    data = (N % (B ** loop)) // (B ** (loop-1))
    result += num_list[data]
    loop += 1
data = (N % (B ** loop)) // (B ** (loop-1))
result += num_list[data]
for item in reversed(list(result)):
    print(item, end="")
