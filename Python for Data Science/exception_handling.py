# EXCEPTION HANDLING = Penanganan error yang terjadi pada saat program dijalankan, sehingga program tidak berhenti secara tiba-tiba (crash) dan dapat memberikan pesan error yang lebih informatif kepada pengguna.

                                # 1. TRY EXCEPT (Penanganan Error)

# misal :
# print(5 + "10")

# solusi :
try : #coba jalan kan ini
    print(5 + "10")
except : #jika terjadi error, maka jalankan ini
    print("Terjadi error, pastikan tipe data yang digunakan benar", '\n') #Output: Terjadi error, pastikan tipe data yang digunakan benar

                                # 2. UNPACKING (*) penanganan error
def jumlah(a, b, c) :
    return a + b + c

data = [1, 2, 3] #list
# makanya pakai * karna fungsi nya untuk membuka isi list satu satu

print(jumlah(*data), '\n') # Output: 6

                                # 3. UNPACKING DI VARIABLE 
nomer = [1,2,3,4,5] 
a, b, *c = nomer #a=1, b=2, c=[3,4,5]

print(a) # Output: 1
print(b) # Output: 2
print(c, '\n') # Output: [3, 4, 5]

                                # 4. ** UNTUK DICTIONARY
def info(nama, umur):
    print(nama, umur)

data = {
    "nama": "Rasky",
    "umur": 21
}

print(info(**data)) # Output: Rasky 21

                # 5. PACKING (*args) kalau jumlah parameter tidak pasti / bebas
def jumlah(*args) :
    return sum(args)

print(jumlah(1, 2, 3)) # Output: 6
print(jumlah(1,2,3,4,5), '\n') # Output: 15

                                # 6. PACKING DICTIONARY 
def biodata(**kwargs) :
    print(kwargs)

print(biodata(nama="Rasky", umur=21, hobi="Coding"), '\n') # Output: {'nama': 'Rasky', 'umur': 21, 'hobi': 'Coding'}

                # 7. ENUMERATE (untuk mendapatkan index dan nilai dari suatu iterable)
kota = ["Jakarta", "Bandung", "Surabaya"]

for i in kota :
    print(i) # Output: Jakarta Bandung Surabaya

for j, item in enumerate(kota) : #j untuk index, item untuk nilai
    print(j, item) # Output: 0 Jakarta 1 Bandung 2 Surabaya

                                # 8. ZIP menggabung 2 list
nama = ["Rasky", "Wijaya", "Jen"]
warna = ["Merah", "Biru", "Putih"]

for n, w in zip(nama, warna) : #n untuk nama, w untuk warna
    print(n, w) # Output: Rasky Merah Wijaya Biru Jen Putih

                                
                                # RINGKASAN SUPER CEPAT
                                    # Materi	Fungsi

# try except    : menangani error
# *list	        : buka isi list
# **dict	    : buka isi dictionary
# *args	        : terima banyak parameter
# **kwargs	    : terima banyak keyword
# enumerate()	: ambil index
# zip()	        : gabung 2 list