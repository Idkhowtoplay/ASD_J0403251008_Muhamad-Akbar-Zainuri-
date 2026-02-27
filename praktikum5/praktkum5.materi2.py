# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# ===========================================================

# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 
def hitung(n): 
    
    if n == 0: 
        print("Selesai") # program mencetak "selesai" ketika n=0
        return
    
    print("Masuk:", n)   # mencetak n hingga 1
    hitung(n-1)          # pemanggilan rekursif
    print("Keluar:", n)  # proses stack unwinding

hitung(3) 