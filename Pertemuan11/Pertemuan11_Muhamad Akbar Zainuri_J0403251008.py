def adjacency_list_dictionary(edges):

    adjacency_list = {}

    # Tambahkan node ke dictionary
    for edge in edges:
        vertex1, vertex2 = edge

        if vertex1 not in adjacency_list:
            adjacency_list[vertex1] = []

        if vertex2 not in adjacency_list:
            adjacency_list[vertex2] = []

        # Tambahkan edge
        adjacency_list[vertex1].append(vertex2)
        adjacency_list[vertex2].append(vertex1)  # karena undirected graph

    # Tampilkan adjacency list
    print("=== ADJACENCY LIST ===")
    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex} -> {neighbors}")


# Testcase
edges1 = [
    ["Bandung", "Yogyakarta"],
    ["Bandung", "Surabaya"],
    ["Bandung", "Bekasi"],
    ["Yogyakarta", "Bali"],
    ["Bali", "Bekasi"],
    ["Bekasi", "Riau"],
    ["Surabaya", "Riau"]
]

adjacency_list_dictionary(edges1)


def create_adjacency_matrix(V, edges):
    # Initialize matrix
    matrix = [[0] * V for _ in range(V)]

    # Populate matrix
    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1  # Undirected graph

    return matrix


# Nama node
nodes = [
    "Bandung",
    "Yogyakarta",
    "Surabaya",
    "Bali",
    "Bekasi",
    "Riau"
]

# Edge berdasarkan index node
edges2 = [
    (0, 1),
    (0, 2),
    (0, 4),
    (1, 3),
    (3, 4),
    (4, 5),
    (2, 5)
]

V1 = 6

adj_matrix1 = create_adjacency_matrix(V1, edges2)

# Tampilkan matrix
print("\n=== ADJACENCY MATRIX ===")
for row in adj_matrix1:
    print(row)