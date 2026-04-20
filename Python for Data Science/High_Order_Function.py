                        # HIGH ORDER FUNCTION : FUNGSI YG PAKAI FUNGSI LAIN

# EXAMPLE : 

                                # A. FUNGSI SEBAGAI PARAMETER 
def kuadrat(x):
    return x * x

def proses(fungsi, angka):
    return fungsi(angka) # memanggil fungsi yang diberikan dengan angka sebagai argumen

print('Contoh fungsi sebagai parameter :')
print(proses(kuadrat, 5),'\n') #output = 25

                                # B. FUNGSI SEBAGAI HASIL KEMBALIAN
                
def pilih(opsi):
    if opsi == 'kali':
        return lambda a, b: a * b
    elif opsi == 'tambah':
        return lambda a, b: a + b
    else:
        return lambda a, b: a - b
    
f = pilih(input('Pilih operasi (kali/tambah/kurang) : '))
print('Contoh fungsi sebagai hasil kembalian :')
print(f(5, 3),'\n') #output tergantung pilihan operasi

# CLOSURE (PENUTUPAN) = Fungsi dalam fungsi yang “ingat” variabel luar

def luar():
    a = 10
    def dalam(x):
        return x + a
    return dalam

f = luar()
print('Contoh closure :')
print(f(5),'\n') #output = 15

# DECORATOR (PEMBUNGKUS FUNGSI) : “nambah fitur ke fungsi tanpa ubah isi" 

def dekorator(f):
    def bungkus():
        print("Sebelum fungsi")
        f()
        print("Sesudah fungsi")
    return bungkus

@dekorator
def halo():
    print("Halo!")

halo()

                                        # 4. MAP, FILTER, REDUCE

# A. MAP = (mengubah semua data)
angka = [1,2,3]

hasil = list(map(lambda x: x * 2, angka)) # mengalikan setiap elemen dengan 2
print('Contoh map :')
print(hasil,'\n') #output = [2, 4, 6]

# B. FILTER = (menyaring data)
angka = [1,2,3,4]

hasil = list(filter(lambda x: x % 2 == 0, angka)) # menyaring angka genap saja
print('Contoh filter :')
print(hasil,'\n') #output = [2, 4]

# C. REDUCE = (menggabungkan data menjadi satu nilai)
from functools import reduce

angka = [1,2,3,4]

hasil = reduce(lambda x, y: x + y, angka) # menjumlahkan semua elemen
print('Contoh reduce :')
print(hasil) #output = 10