import sys

paper_size = int(sys.stdin.readline())
color_paper = [list(sys.stdin.readline().replace("\n", "")) for _ in range(paper_size)]
result = []

def slicing_paper(color_paper):
    result = []
    area1, area2, area3, area4 = [], [], [], []
    for i in range(len(color_paper[0])//2):
        tmp = []
        for j in range(len(color_paper[0])//2):
            tmp.append(color_paper[i][j])
        area1.append(tmp)

    for i in range(len(color_paper[0]) // 2):
        tmp = []
        for j in range(len(color_paper[0]) // 2, len(color_paper)):
            tmp.append(color_paper[i][j])
        area2.append(tmp)


    for i in range(len(color_paper[0]) // 2, len(color_paper[0])):
        tmp = []
        for j in range(len(color_paper[0])//2):
            tmp.append(color_paper[i][j])
        area3.append(tmp)

    for i in range(len(color_paper[0]) // 2, len(color_paper[0])):
        tmp = []
        for j in range(len(color_paper[0]) // 2, len(color_paper[0])):
            tmp.append(color_paper[i][j])
        area4.append(tmp)
    return area4, area3, area2, area1

def recursion(color_paper):
    global result
    flag = color_paper[0][0]
    if len(color_paper[0]) < 2:
        if flag == "1":
            result.append("1")
        elif flag == "0":
            result.append("0")
        return

    for i in range(len(color_paper[0])):
        for j in range(len(color_paper[0])):
            if color_paper[i][j] != flag:
                area4, area3, area2, area1 = slicing_paper(color_paper)
                result.append("(")
                recursion(area4)
                recursion(area3)
                recursion(area2)
                recursion(area1)
                result.append(")")
                return
    if flag == "1":
        result.append("1")
    elif flag == "0":
        result.append("0")
    return

recursion(color_paper)
for item in result:
    print(item, end='')
