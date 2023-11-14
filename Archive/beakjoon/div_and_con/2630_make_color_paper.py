import sys

paper_size = int(sys.stdin.readline())
color_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(paper_size)]
blue, white = 0, 0

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
    global blue, white
    flag = color_paper[0][0]
    if len(color_paper[0]) < 2:
        if flag:
            blue += 1
        else:
            white += 1
        return

    for i in range(len(color_paper[0])):
        for j in range(len(color_paper[0])):
            if color_paper[i][j] != flag:
                area4, area3, area2, area1 = slicing_paper(color_paper)
                recursion(area4)
                recursion(area3)
                recursion(area2)
                recursion(area1)
                return

    if flag:
        blue += 1
    else:
        white += 1
    return

recursion(color_paper)
print(white)
print(blue)
