#-----------------------------------------------------------------
#Nama: Muhamad Akbar Zainuri
#Kelas: J0403251008
#-----------------------------------------------------------------

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis: 
# 1. Lokasi mana yang paling dekat dari Gerbang? Kantin dengan jarak tempuh 2 menit.
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? 7 menit
#    melalui jalur:
#    Gerbang -> Kantin -> Lab -> Aula,  2 + 4 + 1 = 7
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
#    Jalur langsung tidak selalu menghasilkan jarak paling kecil.
#    Terkadang jalur yang melewati beberapa node lain
#    memiliki total bobot yang lebih kecil dibandingkan
#    jalur langsung.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini? 
#    karena semua bobot pada graph bernilai positif
#    dan program membutuhkan pencarian jalur tercepat
#    atau jarak terpendek antar lokasi kampus secara efisien.