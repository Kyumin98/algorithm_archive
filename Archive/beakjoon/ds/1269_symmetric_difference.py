import sys

_input = lambda: sys.stdin.readline()

A_len, B_len = [* map(int, _input().split())]
A_hash, B_hash = {}, {}
A = [* map(int, _input().split())]
B = [* map(int, _input().split())]
for item in A:
    A_hash[item] = 1
for item in B:
    B_hash[item] = 1

cnt = 0
for item in A:
    if not B_hash.get(item):
        cnt += 1
for item in B:
    if not A_hash.get(item):
        cnt += 1
print(cnt)
