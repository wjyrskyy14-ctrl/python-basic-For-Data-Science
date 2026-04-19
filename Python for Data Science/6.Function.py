                                # FUNCTION = blok kode yang bisa dipanggil berkali-kali

# 1. Struktur Function                                
    # def nama_fungsi(parameter):
    #     kode
    #     return hasil

# 2. Function Tanpa Parameter
def halo():
    print("Halo dunia!",'\n')

halo() #output = Halo dunia!

# 3. Function dengan parameter
def sapa(nama):
    print("Halo", nama,'\n')

sapa("Skyyy") #output = Halo Skyyy

# 4. Return
def tambah(a, b):
    return a + b

hasil = tambah(2, 3)
print(hasil,'\n') #output = 5

# 5. Function 2 Parameter
def luas_persegi(panjang, lebar):
    return panjang * lebar

print(luas_persegi(5, 5),'\n') #output = 25

# 6. Default Parameter 
def sapa(nama="Tamu"):
    print("Halo", nama)

sapa()         # Halo Tamu
sapa("Skyyy")  # Halo Skyyy 

# 7. Banyak Argumen 
def jumlah_semua(*angka):
    total = 0 #dipakai untuk menyimpan hasil penjumlahan
    for a in angka: 
        total += a #Ini sama dengan: total = total + a. 
                                      # proses nya total = 0 + 1 → 1
                                                   #total = 1 + 2 → 3
    return total

print(jumlah_semua(1,2,3,4),'\n')  #output = 10

# 8. nama argumen 
def biodata(nama,umur):
    print('nama saya =', nama, 'umur saya :', umur,'\n')

biodata(nama = 'Rasky', umur=21) #output = 

# 9.Return Boolean
def is_even(n):
    return n%2 == 0

print(is_even(4)) #output = True
print(is_even(5),'\n') #output = False

# 10.Return List
def angka_genap(n):
    hasil = [] #dipakai untuk menyimpan angka genap
    for i in range(n+1):
        if i % 2 == 0: #mencetak angka genap saja
            hasil.append(i) #append() = menambahkan ke list. Kalau i genap, masukkan ke hasil
    return  #Mengembalikan isi list

print(angka_genap(10)) #output = [0, 2, 4, 6, 8, 10]
