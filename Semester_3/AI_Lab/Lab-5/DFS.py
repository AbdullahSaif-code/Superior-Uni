# DFS with Stack & Node

"""
             5
           /   \
          3     7
         / \    /
        2   4  8
"""

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': [],
    '8': []
}

visited = []
stack = []

def dfs(graph, start, goal):
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            if node == goal:
                break
            for neighbour in graph[node]:
                stack.append(neighbour)

print("DFS")
dfs(graph, '5', '3')