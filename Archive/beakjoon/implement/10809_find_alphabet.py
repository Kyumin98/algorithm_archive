import sys

_input = lambda : sys.stdin.readline()

N = _input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(N.find(x), end = ' ')
