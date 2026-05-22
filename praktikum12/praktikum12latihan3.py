#-----------------------------------------------------------------
#Nama: Muhamad Akbar Zainuri
#Kelas: J0403251008
#-----------------------------------------------------------------

# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 
 
# Weighted graph dengan bobot negatif 
graph = { 
    'A': {'B': 5, 'C': 4}, 
    'B': {}, 
    'C': {'B': -2} 
} 
 
def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 
 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 
 
        # Periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # Jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    return distances 
 
 
hasil = bellman_ford(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

# Jawaban Analisis: 
# 1. Berapa bobot langsung dari A ke B? 5
# 2. Berapa total bobot jalur A -> C -> B? karena bobot A ke C = 4 dan C ke B = -2, sehingga total = 4 + (-2) = 2
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? A -> C -> B dengan total bobot 2
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
#    karena algoritma ini terus melakukan pembaruan jarak
#    (relaksasi edge) hingga semua kemungkinan jalur diperiksa.
#    Dengan demikian, jarak terpendek tetap bisa ditemukan
#    meskipun terdapat bobot negatif.
# 5. Apa yang dimaksud dengan proses relaksasi edge? 
#    proses memeriksa apakah suatu jalur
#    baru menghasilkan jarak yang lebih kecil dibandingkan
#    jarak yang sudah tersimpan sebelumnya.
#    Jika lebih kecil, maka jarak akan diperbarui.
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    - Bellman-Ford dapat menangani bobot negatif,
#      sedangkan Dijkstra tidak.
#    - Bellman-Ford lebih lambat karena memeriksa semua edge
#      berulang kali.
#    - Dijkstra lebih cepat untuk graph dengan bobot positif.