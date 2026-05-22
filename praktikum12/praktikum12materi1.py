#-----------------------------------------------------------------
#Nama: Muhamad Akbar Zainuri
#Kelas: J0403251008
#-----------------------------------------------------------------

import heapq

# Representasi graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):

    # Menyimpan jarak minimum tiap node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():

            # Hitung jarak baru
            distance = current_distance + weight

            # Update jika jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Menjalankan fungsi dari node A
hasil = dijkstra(graph, 'A')

print(hasil)