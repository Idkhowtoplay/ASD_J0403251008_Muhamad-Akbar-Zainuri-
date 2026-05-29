# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# Praktikum 13 - Graph III: Spanning Tree
# ===========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree? Graph awal memiliki semua edge yang tersedia,
#    sedangkan spanning tree hanya mengambil beberapa edge
#    yang cukup untuk menghubungkan semua simpul tanpa membentuk cycle.

# 2. Mengapa spanning tree tidak boleh memiliki cycle? Spanning tree tidak boleh memiliki cycle karena tujuan spanning tree
#    adalah menghubungkan semua node dengan jalur paling sederhana.
#    Jika ada cycle, maka graph bukan tree lagi.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit? Jumlah edge spanning tree selalu lebih sedikit karena
#    spanning tree hanya membutuhkan edge minimum untuk
#    menghubungkan semua node. Untuk n node, spanning tree
#    selalu memiliki n - 1 edge.