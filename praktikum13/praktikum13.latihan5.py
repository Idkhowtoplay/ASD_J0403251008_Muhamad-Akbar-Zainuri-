# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# Praktikum 13 - Graph III: Spanning Tree
# ===========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

# Proses algoritma Kruskal sederhana
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle
    if u not in connected or v not in connected:

        mst.append((u, v, weight))

        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:\n")

for edge in mst:
    print(edge)

# Menampilkan total bobot
print("\nTotal bobot minimum =", total_weight)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Kasus apa yang dipilih? Kasus 2 - Jaringan Komputer.

# 2. Algoritma apa yang digunakan? Kruskal.
#    Karena Kruskal memilih edge dengan bobot terkecil
#    secara bertahap untuk membentuk MST.

# 3. Edge mana saja yang dipilih dalam MST?
#    - RouterC -> RouterD = 1
#    - RouterA -> RouterC = 2
#    - RouterA -> RouterB = 3

# 4. Berapa total bobot MST? 1 + 2 + 3 = 6

# 5. Mengapa edge tertentu tidak dipilih? Edge tertentu tidak dipilih karena dapat membentuk cycle
#    atau sudah ada jalur lain yang menghubungkan router,
#    sehingga edge tersebut tidak diperlukan lagi.