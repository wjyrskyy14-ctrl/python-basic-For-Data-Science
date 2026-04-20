# LIST COMPREHENSION = List comprehension itu sebenarnya cuma cara singkat dari for loop.

                            # POLA UMUM (SYNTAX NYA):

#             'if kondisi' = filter untuk menyaring item
# [hasil for item in data if kondisi]

# penjelsan = 'hasil' = mau ngapain datanya
#             'for item in data' = (looping) untuk setiap item di data


#    EXAMPLE :
angka = [] #list kosong untuk menampung 

# cara biasa (loop biasa) :
for i in range(5):
    angka.append(i)
print('cara biasa :')
print(angka,'\n') #output = [0, 1, 2, 3, 4]

# cara dengan list comprehension : membuat lebih ringkas dan lebih mudah dibaca
angka = [i for i in range(5)]
print('cara list comprehension :')
print(angka,'\n') #output = [0, 1, 2, 3, 4]

# contoh kuadrat
kuadrat = [i*i for i in range(5)]
print('Contoh kuadrat :')
print(kuadrat,'\n') #output = [0, 1, 4, 9, 16]

# contoh genap
genap = [i for i in range(10) if i % 2 == 0]
print('Contoh bilangan genap :')
print(genap,'\n') #output = [0, 2, 4, 6, 8]

# FLATTEN = proses mengubah list yang berisi list menjadi list datar (flat list)
list_of_lists = [[1,2,3],[4,5,6]]

hasil = [num for row in list_of_lists for num in row] #
print('Contoh flatten :')
print(hasil,'\n') #output = [1, 2, 3, 4, 5, 6]


# LAMBDA FUNCTION = Lambda function adalah fungsi anonim yang dapat dibuat dengan cepat tanpa harus mendefinisikan fungsi secara formal menggunakan def.

# FUNGSI BIASA : 
def tambah(a, b):
    return a + b
print('Contoh fungsi biasa :')
print(tambah(2, 3)) #output = 5

# VERSI LAMBDA :
tambah = lambda a, b: a + b
print('Contoh fungsi lambda :')
print(tambah(2, 3)) #output = 5

# LAMBDA DALAM FUNGSI(FUNCTION)
def pangkat(n):
    return lambda n: n**n

empat_pangkat_3 = pangkat(4)(3)
print('Contoh pangkat :')
print(empat_pangkat_3) #output = 64