# BFS without Queue & Node

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'F': ['H']
}

def bfs(graph, start, goal):
    visited = []
    current_level = [start]

    while current_level:
        next_level = []
        for node in current_level:
            if node not in visited:
                visited.append(node)
                print(node, end=" ")

                if node == goal:
                    print(f"\nGoal node {goal} found!")
                    return True

                next_level.extend(graph.get(node, []))
        current_level = next_level

    print("\nGoal node not found.")
    return False

print("BFS Search:")
bfs(graph, 'A', 'E')
