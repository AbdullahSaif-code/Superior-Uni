# BFS without Queue & Node

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'F': ['H']
}

visited = []

def bfs_recursive(graph, node, goal):
    visited.append(node)
    print(node, end=" ")

    if node == goal:
        print(f"\nGoal node {goal} found!")
        return True

    for neighbour in graph.get(node, []):
        if neighbour not in visited:
            if bfs_recursive(graph, neighbour, goal):
                return True

print("BFS Search:")
bfs_recursive(graph, 'A', 'E')
