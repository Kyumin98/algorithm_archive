import sys

_input = lambda : sys.stdin.readline()

word = _input().replace("\n", "")
word_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in word_list:
    word = word.replace(i, '*')
print(len(word))
