# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# ===========================================================

# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 
def pangkat(a, n): 
# Base case 
    if n == 0:  #Jika n adalah 0 maka fungsi akan mereturn angka 1
        return 1 
    
# Recursive case 
 # Recursive case
    # Jika n tidak sama dengan 0 maka fungsi akan memanggil dirinya sendiri
    # Nilai n dikurangi 1 setiap pemanggilan sampai akhirnya mencapai 0
    # Setiap pemanggilan akan mengalikan a dengan hasil dari pemanggilan berikutnya
    return a * pangkat(a, n - 1) 


# Pemanggilan fungsi
# Menghitung 2 pangkat 4 yang berarti 2 x 2 x 2 x 2
print(pangkat(2, 4))  # Output: 16