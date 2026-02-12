print("1")
buah= ["apel", "jeruk", "mangga", "melon"]
print(buah, '\n')

print("2")
hewan = ['kucing', 'anjing', 'ular', 'burung']
print(hewan[1],'\n')  

print("3")
hewan_2 = ['kucing', 'anjing', 'ular', 'burung']
hewan_2[2] = "singa"
print(hewan_2)  

print("4")
buah_2 = ['apel', 'jeruk']#
buah_2.append("semangka")
print(buah_2)

print("extend")
tambah = ['mangga', 'pisang']
buah_2.extend(tambah)
print(buah_2)

print("5")
buah_3 = ['apel', 'jeruk', 'semangka']
buah_3.remove("jeruk")
print(buah_3)

print("6")
angka = [5, 10, 15, 20, 25]
print(len(angka))

print("7")
nilai = [80, 75, 90, 60, 85]
print(nilai[:3])  # Output: [80, 75, 90]

print("8")
warna = ['merah', 'kuning', 'hijau', 'biru']
print(warna[-1])  

print("9")
a = [1, 2, 3]
b = [4, 5]
print(a + b)# 

print("10")
kuadrat = [(i**2) for i in range(1,6)]
print(kuadrat)

# LATIHAN LIST COMPREHENSION

print("11")
angka = [1, 2, 3, 4, 5, 6]
genap = [i for i in angka if i % 2 == 0]
print(genap)

print("12")
kata = ['apel', 'jeruk', 'melon']
panjang_kata = [len(i) for i in kata]
print(panjang_kata)

print("13")
buah = ['mangga', 'pisang', 'salak']
kapital = [i.capitalize() for i in buah]
print(kapital)

print("14")
hewan = ['kuda', 'sapi', 'kucing', 'anjing']
empathuruh = [i for i in hewan if len(i) >4]
print(empathuruh)

print("15")
print([i for i in range(10) if i % 2 == 0])



# OPERASI LIST

print("Contoh count()")

angka = [1,2,3,3,3,5,4,2,2,5,8,9,1,1,4]

jumlah_angka_3 = angka.count(3)
jumlah_angka_1 = angka.count(1)

print("Jumlah angka 3:", jumlah_angka_3)
print("Jumlah angka 1:", jumlah_angka_1)


print("contoh index()") #mencari index dari suatu nilai dalam list
buah = ['apel', 'jeruk', 'mangga', 'melon', 'durian']

index_melon = buah.index('melon')
index_jeruk = buah.index('jeruk')

print("Index melon:", index_melon)
print("Index jeruk:", index_jeruk)


print("contoh sort()")
print("Sebelum di sort:", angka)

angka.sort()
buah.sort()
print("Setelah di sort:", angka)
print("Setelah di sort:", buah)

print("contoh reverse()")
angka.reverse()
buah.reverse()

print("Setelah di reverse:", angka)
print("Setelah di reverse:", buah)



# MATERI COPY list

print("contoh copy list")
a = ["Rasky", "Ronaldo", "Mbappe", "Ole"]
b = a

print(f"nama data a = \n {a}")
print(f"nama data b = \n {b}")

a[2] = "balik"
print(f"nama data b = \n {a}")
print(f"nama data b = \n {b}")

# agar tidak ikut berubah harus di tambahkan method copy()

print("contoh copy list dengan method copy()")
a = ["Rasky", "Ronaldo", "Mbappe", "Ole"]
b = a.copy()

b[2] = "balik"
print(f"nama data a = \n {a}")
print(f"nama data b = \n {b}")




# NESTED LIST

# JADI SUATU LIST DI DALAM LIST LAINNYA

print("\ncontoh nested list")

peserta_0 = ["Rasky", 20, "Laki-laki"]
peserta_1 = ["Ronaldo", 19, "Perempuan"]
peserta_2 = ["Mbappe", 8, "Perempuan"]
peserta_3 = ["Ole", 5, "Laki-laki"]

data_peserta =[peserta_0, peserta_1, peserta_2, peserta_3]
print(" jadi data peserta = ",data_peserta)

for peserta in data_peserta:
    print(f"\nnama \t\t: {peserta[0]}")
    print(f"umur \t\t: {peserta[1]}")
    print(f"jenis kelamin \t: {peserta[2]}")


