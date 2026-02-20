# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# ===========================================================

# ===========================================================
# Implementasi Dasar : stack 
# ===========================================================

class Node:
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#stack ada operasi push(memasukkan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
    
    def is_empty(self):
        return self.top is None #stack kosong jika top = None

    def push(self,data):
        #1 membuat code baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class node

        #2 node baru menunjuk ke top yang lama (node lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #Mengambil / menghapus node paling atas (top/head)
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        self.top = self.top.next 
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data
        
    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("Top ->" , end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
s.pop()
