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

    # Tampilkan adjacency list
    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex} -> {neighbors}")


# Testcase
edges1 = [
    ["A", "B"],
    ["A", "C"],
    ["B", "A"],
    ["B", "D"],
    ["C", "A"],
    ["C", "D"],
    ["D", "B"],
    ["D", "C"]
]

adjacency_list_dictionary(edges1)