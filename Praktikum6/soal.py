#-----------------------------------------------------------------
#Nama: Muhamad Akbar Zainuri
#Kelas: J0403251008
#-----------------------------------------------------------------

#Ascending
def budi(data):
    for l in range(len(data)-1,0,-1):
        for i in range(l):
            if data[i]<data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
a = data
budi(data)
print("Skor lima kandidat tertinggi: ", data[:5])
for i in data[:5]:
    if i in a:
        print(i, "Index ke: ",a.index(i))