# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# Praktikum 13 - Graph III: Spanning Tree
# ===========================================================

import heapq

graph = {
 'A': {'B': 4, 'C': 2, 'D': 5},
 'B': {'A': 4, 'D': 3},
 'C': {'A': 2, 'D': 1},
 'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start])

    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edge:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
 print(edge)

print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan? Node awal yang digunakan adalah node 'A'.

# 2. Edge mana yang dipilih pertama kali? ('A', 'C', 2) karena memiliki bobot paling kecil
#    dari semua edge yang terhubung ke node A.

# 3. Bagaimana Prim menentukan edge berikutnya? dengan memilih edge berbobot paling kecil 
#    yang menghubungkan node yang sudah dikunjungi 
#    dengan node yang belum dikunjungi.

# 4. Berapa total bobot MST yang dihasilkan? 2 + 1 + 3 = 6

# 5. Apa perbedaan pendekatan Prim dan Kruskal? 
#    - Prim memulai dari satu node lalu memperluas tree sedikit demi sedikit.
#    - Kruskal memilih edge terkecil secara global tanpa memulai dari node tertentu.
#    - Prim fokus pada node yang sudah terhubung, sedangkan Kruskal fokus pada pengurutan edge.