                                                    # loop

# Hidup ini penuh dengan rutinitas.Dalam pemrograman kami juga melakukan banyak tugas yang berulang.Untuk menangani tugas yang berulang, bahasa pemrograman menggunakan loop.Bahasa pemrograman Python juga menyediakan dua jenis loop berikut:

# 1. perulangan sementara
# 2. untuk lingkaran

# 1. FOR LOOP 
for i in range(6):
    print(i,'\n') # output: 0, 1, 2, 3, 4, 5

# 2. RANGE 
for i in range(2, 8): # START, STOP
    print('ini contoh for loop (START, STOP) :',i) # output: 2, 3, 4, 5, 6, 7

for i in range(0, 10, 2): # START, STOP, STEP
    print('ini contoh for loop (START, STOP, STEP) :',i) # output: 0, 2, 4, 6, 8


                                                # While Loop
# Kami menggunakan kata khusus _sementara_ untuk membuat perulangan while.
# Ini digunakan untuk mengeksekusi blok pernyataan berulang kali hingga kondisi tertentu terpenuhi.
# Ketika kondisi menjadi salah, baris kode setelah perulangan akan terus dieksekusi.

count = 0

while count < 5: 
    count += 1
    print('ini contoh while loop :',count) # menambahkan nilai count sebanyak 1 setiap iterasi

                                        # BREAK : Menghentikan loop langsung.

for i in range(10):
    if i == 5:
        break
    print('ini contoh break :',i) # output: 0, 1, 2, 3, 4

                                # CONTINUE : Skip iterasi saat ini, lanjut ke berikutnya.

for i in range(5):
    if i == 2:
        continue
    print('ini contoh continue :',i) # output: 0, 1, 3, 4 (melewati angka 2)

                                            # LOOPS DI LIST 

buah = ['apel', 'jeruk', 'mangga']
for i in buah:
    print('ini contoh loops di list :',i) # output: apel, jeruk, mangga

                                            #LOOPS DI STRING

nama = 'Rasky'
for i in nama:
    print('ini contoh loops di string :',i) # output: R, a, s, k, y

                                        # LOOPS DI DICTIONARY

nama = {
    'nama_depan': 'Rasky',
    'nama_belakang': 'Wijaya',
    'umur': 21
}
for key, value in nama.items():
    print('loops dictionary :', key, value) # output: nama_depan : Rasky, nama_belakang : Wijaya, umur : 21
