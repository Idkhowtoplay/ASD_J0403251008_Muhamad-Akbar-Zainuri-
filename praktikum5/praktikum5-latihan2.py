# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# ===========================================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ==========================================================

def countdown(n): # inisialisasi fungsi countdown
 
    if n == 0: #jika n sama dengan 0 maka print selesai dan return
        print("Selesai") 
        return 
 
    print("Masuk:", n) 
    countdown(n - 1) #call rekurrsif sampai n sama dengan 0

    # Baris ini dijalankan setelah pemanggilan rekursif selesai
    # Artinya program sedang kembali ke atas satu per satu
    # Karena kembali dari pemanggilan terakhir, maka angka yang dicetak
    # akan muncul dari yang paling kecil menuju yang paling besar
    print("Keluar:", n)

countdown(3) 
