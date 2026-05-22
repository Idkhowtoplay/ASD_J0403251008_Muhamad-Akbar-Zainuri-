#-----------------------------------------------------------------
#Nama: Muhamad Akbar Zainuri
#Kelas: J0403251008
#-----------------------------------------------------------------

# ==========================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Representasi graph berbobot menggunakan dictionary
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek
    dari node awal ke semua node lain
    menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak sekarang lebih besar dari data sebelumnya
        # maka dilewati
        if current_distance > distances[current_node]:
            continue

        # Mengecek semua tetangga node
        for neighbor, weight in graph[current_node].items():

            # Menghitung total jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:

                # Update jarak
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menjalankan algoritma dari node Bogor
hasil = dijkstra(graph, 'Bogor')

# Output hasil jarak terpendek
print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Node awal yang digunakan adalah Bogor.

# 2. Node yang memiliki jarak paling kecil dari node awal
#    adalah Depok dengan jarak 2.

# 3. Node yang memiliki jarak paling besar dari node awal
#    adalah Bandung dengan jarak 8.

# 4. Algoritma Dijkstra bekerja dengan cara memilih node
#    yang memiliki jarak sementara paling kecil,
#    kemudian memperbarui jarak ke node tetangganya
#    hingga ditemukan jarak terpendek ke semua node.