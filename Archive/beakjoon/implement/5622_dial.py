import sys

_input = lambda : sys.stdin.readline()

dict = {
    3: ["A", "B", "C"],
    4: ["D", "E", "F"],
    5: ["G", "H", "I"],
    6: ["J", "K", "L"],
    7: ["M", "N", "O"],
    8: ["P", "Q", "R", "S"],
    9: ["T", "U", "V"],
    10: ["W", "X", "Y", "Z"]
}
cnt = 0

data = _input().replace("\n", "")
data_list = list(data)
for item in data_list:
    for idx in range(3, 11):
        if item in dict[idx]:
            cnt += idx
print(cnt)
