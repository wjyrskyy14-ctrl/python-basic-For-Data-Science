                                        # CLASS & object 

# PENJELASAN : 
# class = cetakan / blueprint. ex = Mahasiswa 
# object = hasil jadi dri cetakan itu. ex = Rasky, Steven, Wijaya

                                        
                                        # 1. Contoh 2 
class Mahasiswa :
    def __init__(self, nama, umur): # __init__ = constructor, digunakan untuk menginisialisasi atribut pada saat pembuatan object, self = parameter pertama pada method dalam class yang merujuk pada instance objek itu sendiri, nama dan umur = parameter yang akan diisi saat membuat object
        self.nama = nama # self.nama = atribut nama, nama = parameter nama
        self.umur = umur # self.umur = atribut umur, umur = parameter umur

mhs1 = Mahasiswa("Rasky", 20) # membuat object mhs1 dari class Mahasiswa dengan nilai atribut nama = "Rasky" dan umur = 20
print(mhs1.nama) # Output: Rasky
print(mhs1.umur,'\n') # Output: 20


                                        # 2. METHOD = fungsi dalam class 
class Mahasiswa :
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur 

    def perkenalan(self): # method perkenalan, digunakan untuk memperkenalkan diri dengan mencetak nama dan umur
        print("halo nama saya", self.nama)

mhs2 = Mahasiswa('Rasky', 21) # membuat object mhs2 dari class Mahasiswa dengan nilai atribut nama = "Rasky" dan umur = 21
print(mhs2.perkenalan()) # Output: halo nama saya Rasky (method perkenalan dipanggil untuk object mhs2, mencetak "halo nama saya Rasky")


                                        # 3. DEFAULT VALUE = nilai bawaan 
class Mahasiswa :
    def __init__(self, nama="tanpa nama"): # parameter nama memiliki default value "tanpa nama", sehingga jika tidak diberikan nilai saat membuat object, maka akan menggunakan default value ini
        self.nama = nama

mhs3 = Mahasiswa() # membuat object mhs3 dari class Mahasiswa tanpa memberikan nilai untuk parameter nama, sehingga akan menggunakan default value "tanpa nama"
print(mhs3.nama,'\n') # Output: tanpa nama (karena default value digunakan)


                                        # 4. METHOD UNTUK MENAMBAH DATA 
class Mahasiswa :
    def __init__(self, nama):
        self.nama = nama
        self.hobi = [] # atribut hobi diinisialisasi sebagai list kosong untuk menyimpan hobi-hobi mahasiswa

    def tambah_hobi(self, hobi_baru): # method tambah_hobi, digunakan untuk menambahkan hobi baru ke dalam list hobi mahasiswa
        self.hobi.append(hobi_baru) # menambahkan hobi baru ke dalam list hobi menggunakan method append()

mhs4 = Mahasiswa("Rasky") # membuat object mhs4 dari class Mahasiswa dengan nilai atribut nama = "Rasky"
mhs4.tambah_hobi("Coding") # menambahkan hobi "Coding" ke dalam list hobi mahasiswa mhs4 menggunakan method tambah_hobi
mhs4.tambah_hobi("Gaming") # menambahkan hobi "Gaming" ke

print(mhs4.hobi,'\n') # Output: ['Coding', 'Gaming'] (mencetak list hobi mahasiswa mhs4 yang telah ditambahkan dengan hobi "Coding" dan "Gaming")


                                        # 5. INHERITANCE = pewarisan
class manusia:
    def salam(self):
        print("halo dari manusia")

class Mahasiswa(manusia): # class Mahasiswa mewarisi class manusia, sehingga dapat menggunakan method salam() dari class manusia
    pass # kosong atau tidak ada isi

s1 = Mahasiswa() # membuat object s1 dari class Mahasiswa
s1.salam() # Output: halo dari manusia (method salam() dipanggil untuk object s1, mencetak "halo dari manusia" karena class Mahasiswa mewarisi method salam() dari class manusia)


                                            # RANGKUMAN : 
                                # Inti Besar Materi Ini = Wajib hafal ini:
# Class = cetakan
# Object = hasil dari cetakan
# init = constructor
# self = object itu sendiri
# method = function di dalam class
# inheritance = pewarisan class