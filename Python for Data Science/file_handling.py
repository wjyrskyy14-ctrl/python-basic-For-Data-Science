                # FILE HANDLING = baca data, simpan data, update data, hapus data, dll.

                                # 1. MEMBUKA FILE = open("nama_file", "mode")

# MODE PADA FILE (yg wajib di hafal)
        # | Mode | Arti                              |
        # | ---- | --------------------------------- |
        # | r    | read (membaca)                    |
        # | w    | write (menulis, menimpa isi lama) |
        # | a    | append (menambah di akhir file)   |
        # | x    | create (buat file baru)           |
        # | t    | text                              |
        # | b    | binary                            |

                                # 2. MEMBACA FILE = r 

# a. read() = membaca seluruh isi file
f = open("data.txt", "r")
print(f.read(),'\n') # Output: Halo dunia, Saya belajar Python, Ini adalah contoh file untuk materi File Handling.
f.close() # jangan lupa tutup file setelah selesai

# b. read(10) = membaca 10 karakter pertama
f = open("data.txt", "r")
print(f.read(10),'\n') # Output: Halo dunia
f.close() #supaya file tidak menggantung

# c. readline() = membaca satu baris
f = open("data.txt", "r")
print(f.readline(),'\n') # Output: Halo dunia
f.close() #supaya file tidak menggantung

# d. readlines() = membaca semua baris dan mengembalikan dalam bentuk list
f = open("data.txt", "r")
print(f.readlines(),'\n') # Output: ['Halo dunia, Saya belajar Python, Ini adalah contoh file untuk materi File Handling.']
f.close() #supaya file tidak menggantung

# CARA LEBIH AMAN DENGAN WITH AS (tidak perlu tutup file, karena dengan with as file akan otomatis tertutup setelah selesai)
with open("data.txt", "r") as f :
    print(f.read(),'\n') # Output: Halo dunia, Saya belajar Python, Ini adalah contoh file untuk materi File Handling.

                                # 3. MENULIS FILE = w (menulis, menimpa isi lama)
with open("data.txt", "w") as f :
    f.write("Rasky pintar coding") # Output: Rasky pintar coding (isi file akan berubah menjadi ini, karena mode w menimpa isi lama)

                                # 4. MENAMBAH ISI/FILE = a (menambah di akhir file)
with open("data.txt", "a") as f :
    f.write("\ndan akan menjadi orang yg sukses") # Output: Rasky pintar coding, dan akan menjadi orang yg sukses (isi file akan bertambah di akhir file, karena mode a menambah di akhir file)

                                #5. MENGHAPUS FILE 
import os 

os.remove("data.txt") # Output: file data.txt akan terhapus dari direktori, karena os.remove() digunakan untuk menghapus file dari sistem operasi. Pastikan untuk berhati-hati saat menggunakan fungsi ini, karena file yang dihapus tidak dapat dikembalikan.

                                # 6. CEK FILE ADA ATAU TIDAK 
if os.path.exists("data.txt") : # Python disuruh mengecek: “Apakah file bernama data.txt ada?” seperti True / False. jika True maka disuruh hapus file, jika False maka kasih tau file tidak ada
    os.remove("data.txt")
else :
    print("file tidak ada")

                                # 7. JSON = mirip dictionary
import json

# a. DICTIONARY KE JSON
person = {
    "name": "Sky",
    "age": 20,
    "country": "Indonesia"
}
person_json = json.dumps(person, indent=4) # dumps = ubah jadi string json
                                           # indent=4 untuk membuat json lebih rapi dan mudah dibaca dengan menambahkan indentasi 4 spasi pada setiap level struktur data dalam output JSON.
print(person_json)

# b. JSON KE DICTIONARY 
data = '''
{
    "nama": "Rasky",
    "umur": 21,
    "hobi": ["Coding", "Gaming", "Traveling"]
}
'''

person = json.loads(data)