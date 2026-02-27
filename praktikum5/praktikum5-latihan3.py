# ===========================================================
# Nama  : Muhamad Akbar Zainuri
# NIM   : J0403251008
# Kelas : TPL A1 
# ===========================================================

# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
def cari_maks(data, index=0): 
 
    # Base case 
    if index == len(data) - 1: #jika index sama dengan panjang data dikurang 1 maka return list[index]
        return data[index] 
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) # memanggil fungsi rekursif di variabel maks_sisa
 
    if data[index] > maks_sisa: #jika element dalam list lebih dari variabel maks sisa maka return data[index]
        return data[index] 
    else: 
        return maks_sisa 
 
 
angka = [3, 7, 2, 9, 5] #list
print("Nilai maksimum:", cari_maks(angka)) #cetak nilai maks