# Adjacency Matrix
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

# Konversi ke Adjacency List
adj_list = {}

for i in range(len(matrix)):
    adj_list[i] = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            adj_list[i].append(j)

# Tampilkan hasil
print("Adjacency List:")
for key, value in adj_list.items():
    print(f"{key}: {value}")