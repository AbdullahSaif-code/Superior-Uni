"""
             A
           /   \
          B     C
         / \    /
        D   E--F
"""
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = []
stack = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end = " ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
dfs(visited, graph, 'F')

print("\n")
def output_graph(graph):
    for node in graph:
        print(node, ":", graph[node])
output_graph(graph)