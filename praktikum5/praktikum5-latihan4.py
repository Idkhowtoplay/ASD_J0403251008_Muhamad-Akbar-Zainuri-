# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# ===========================================================

# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""): 
 
    if len(hasil) == n: # Jika panjang hasil sama dengan n maka print hasil
        print(hasil) 
        return 
    
    # Recursive call pertama
    # Menambahkan huruf A ke dalam hasil
    # Lalu fungsi dipanggil kembali untuk melanjutkan pembentukan huruf berikutnya
    kombinasi(n, hasil + "A") 

     # Recursive call kedua
    # Menambahkan huruf B ke dalam hasil
    # Lalu fungsi dipanggil kembali untuk melanjutkan pembentukan huruf berikutnya
    kombinasi(n, hasil + "B") # Recursif call kedua
 
kombinasi(2) # Pemanggilan fungsi dengan argumen 2