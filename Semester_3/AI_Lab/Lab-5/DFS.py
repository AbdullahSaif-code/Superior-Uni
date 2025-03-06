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

def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            if node == goal:
                break
            stack.extend(graph[node][::-1])  # Add neighbors in reverse order to maintain correct order

print("DFS")
dfs(graph, '5', '8')
