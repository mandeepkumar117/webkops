# Number of vertices
vertices = int(input("Enter number of vertices: "))

# Number of edges
edges = int(input("Enter number of edges: "))


# Empty graph
graph = {}


# Vertices input
for i in range(vertices):

    vertex = input("Enter vertex: ")

    graph[vertex] = []


# Edges input
for i in range(edges):

    u = input("Enter first vertex: ")
    v = input("Enter second vertex: ")

    graph[u].append(v)
    graph[v].append(u)


# Print graph
print("\nGraph:")

for vertex in graph:
    print(vertex, "->", graph[vertex])