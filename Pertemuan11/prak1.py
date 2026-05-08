def create_adjacency_matrix(V, edges):
    # Initialize an empty V x V matrix with all zeros
    matrix = [[0] * V for _ in range(V)]
    
    # Populate the matrix based on the edges
    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1  # Undirected graph
    
    return matrix


# Example 1
V1 = 4
edges1 = [(0, 1), (0, 2), (1, 2), (2, 3)] #list edges
adj_matrix1 = create_adjacency_matrix(V1, edges1) # panggil fungsi dan simpan di variabel adj_matrix1
for row in adj_matrix1: #looping variabel adj_matrix
    print(row) 
