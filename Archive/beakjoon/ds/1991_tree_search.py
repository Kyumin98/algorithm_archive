import sys

N = int(sys.stdin.readline())
graph = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
stack = []

def recursion(graph, current_node, depth):
    global stack
    if graph[depth][1] == "." and graph[depth][2] == ".":
        stack.append(current_node)
        return

    stack.append(current_node)
    if graph[depth][1] != ".":
        for i in range(depth, len(graph)):
            if graph[i][0] == graph[depth][1]:
                recursion(graph, graph[depth][1], i)

    if graph[depth][2] != ".":
        for i in range(depth, len(graph)):
            if graph[i][0] == graph[depth][2]:
                recursion(graph, graph[depth][2], i)
                break

    return
def recursion2(graph, current_node, depth):
    global stack
    if graph[depth][1] == "." and graph[depth][2] == ".":
        stack.append(current_node)
        return

    if graph[depth][1] != ".":
        for i in range(depth, len(graph)):
            if graph[i][0] == graph[depth][1]:
                recursion2(graph, graph[depth][1], i)
    stack.append(current_node)
    if graph[depth][2] != ".":
        for i in range(depth, len(graph)):
            if graph[i][0] == graph[depth][2]:
                recursion2(graph, graph[depth][2], i)
                break
    return

def recursion3(graph, current_node, depth):
    global stack
    if graph[depth][1] == "." and graph[depth][2] == ".":
        stack.append(current_node)
        return

    if graph[depth][1] != ".":
        for i in range(depth, len(graph)):
            if graph[i][0] == graph[depth][1]:
                recursion3(graph, graph[depth][1], i)
    if graph[depth][2] != ".":
        for i in range(depth, len(graph)):
            if graph[i][0] == graph[depth][2]:
                recursion3(graph, graph[depth][2], i)
                break
    stack.append(current_node)
    return

recursion(graph, "A", 0)
for item in stack:
    print(item, end='')
print()
stack = []
recursion2(graph, "A", 0)
for item in stack:
    print(item, end='')
print()
stack = []
recursion3(graph, "A", 0)
for item in stack:
    print(item, end='')
