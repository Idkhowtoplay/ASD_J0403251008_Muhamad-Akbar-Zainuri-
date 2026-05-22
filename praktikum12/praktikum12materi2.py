#-----------------------------------------------------------------
#Nama: Muhamad Akbar Zainuri
#Kelas: J0403251008
#-----------------------------------------------------------------

def bellman_ford(graph, start):

    # Membuat dictionary untuk menyimpan
    # jarak minimum setiap node
    # Awalnya semua bernilai tak hingga (infinity)
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Proses relaksasi dilakukan sebanyak
    # jumlah node - 1
    for _ in range(len(graph) - 1):

        # Menelusuri setiap node pada graph
        for node in graph:

            # Mengambil tetangga dan bobot edge
            for neighbor, weight in graph[node].items():

                # Menghitung kemungkinan jarak baru
                if distances[node] + weight < distances[neighbor]:

                    # Jika lebih kecil, update jarak
                    distances[neighbor] = distances[node] + weight

    # Mengembalikan hasil jarak terpendek
    return distances


# Representasi graph
# Format:
# 'Node': {'Tetangga': bobot}
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menjalankan algoritma Bellman-Ford
# dengan node awal A
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil akhir
print("Jarak terpendek dari node A:")
print(hasil)