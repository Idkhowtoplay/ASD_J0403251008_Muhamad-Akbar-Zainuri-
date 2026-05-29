# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# Praktikum 13 - Graph III: Spanning Tree
# ===========================================================

import heapq

# Representasi graph
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    visited = set([start])

    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_cost = 0

    # Proses pencarian MST
    while edges:

        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))

            total_cost += weight

            # Menambahkan edge baru ke priority queue
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_cost


# Menjalankan algoritma Prim
mst, total = prim(graph, 'GedungA')

# Menampilkan hasil
print("Minimum Spanning Tree:\n")

for edge in mst:
    print(edge)

print("\nTotal biaya minimum =", total)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Algoritma apa yang digunakan? Prim karena Prim cocok digunakan untuk mencari
#    jaringan minimum dengan memulai dari satu node
#    lalu memperluas koneksi dengan biaya terkecil.

# 2. Edge mana saja yang dipilih?
#    - GedungA -> GedungC = 2
#    - GedungC -> GedungD = 1
#    - GedungD -> GedungB = 3

# 3. Berapa total biaya minimum? 2 + 1 + 3 = 6

# 4. Mengapa MST cocok digunakan pada kasus ini? MST cocok digunakan karena dapat menghubungkan
#    semua gedung dengan total biaya pemasangan kabel
#    paling minimum tanpa membentuk cycle.