import sys

_input = lambda : sys.stdin.readline()

def prefix():
    prefix = [0 for i in range(0, len(P))]

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = prefix[j - 1]

        if (P[i] == P[j]):
            j += 1
            prefix[i] = j
    return prefix


def solution(prefix):
    result = []
    count = 0

    j = 0
    for i in range(0, len(T)):

        while j > 0 and T[i] != P[j]:
            j = prefix[j - 1]

        if T[i] == P[j]:
            if j == (len(P) - 1):
                result.append(i - len(P) + 2)
                count += 1
                j = prefix[j]
            else:
                j += 1

    print(count)
    for item in result:
        print(item)


T = list(_input().replace("\n", ""))
P = list(_input().replace("\n", ""))
solution(prefix())
