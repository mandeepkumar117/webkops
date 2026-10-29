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


def bfs(graph, start):

    queue = []
    visited = []

    queue.append(start)
    visited.append(start)

    while len(queue) > 0:

        current = queue[0]
        queue = queue[1:]

        print(current, end=" ")

        for neighbor in graph[current]:

            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


start = int(input("Enter starting vertex: "))

print("BFS Traversal:")

bfs(graph, start)