# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# ===========================================================

# ===========================================================
# Implementasi Dasar : kode pada Linked List
# ===========================================================

class Node:
    #Konstruktor yang dijalankan secara otomatis ketik class node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

nodeA = Node("A")
nodeB = Node("B")
nodec = Node("c")

#2) Menghubungkan Node : A-> B -> C -> None
head = nodeA
nodeA.next = nodec

#3) Traversal : Menelusuri node dari head sampai ke None'
current = head
while current is not None:
    print(current.data) #Menampilkan data pada Node sat
    current = current.next #pindah ke Node berikutnya 