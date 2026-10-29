vertices = int(input("Enter number of vertices: "))

graph = {}

for i in range(vertices):
    vertex = int(input("Enter vertex: "))
    graph[vertex] = []

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))

    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, current, visited):

    visited.append(current)

    print(current, end=" ")

    for neighbor in graph[current]:

        if neighbor not in visited:

            dfs(graph, neighbor, visited)


start = int(input("Enter starting vertex: "))

visited = []

print("DFS Traversal:")

dfs(graph, start, visited)