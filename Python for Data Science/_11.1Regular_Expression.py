                # REGULAR EXPRESSION = alat pencari pola dalam teks

import re # module regular expression

                    # 1. MATCH (harus dari awal) 
teks = "Halo, nama saya Rasky"
hasil = re.match("Halo, nama", teks) # Output: <re.Match object; span=(0, 10), match='Halo, nama'> match() digunakan untuk mencari pola yang cocok dengan teks dari awal string.
print(hasil)

                    # 2. SEARCH (bisa dari mana saja)
hasil2 = re.search("saya Rasky", teks) # Output: <re.Match object; span=(11, 24), match='saya Rasky'> search() digunakan untuk mencari pola yang cocok dengan teks dari mana saja dalam string.
print(hasil2)

                    # 3. FINDALL (mencari semua pola yang cocok)
teks2 = "saya suka mba j, Saya suka mba j, saYa suka mba j"
hasil3 = re.findall("saya",teks2, re.I) #re.I = ignore case (tidak memperhatikan huruf besar kecil) Output: ['saya', 'Saya', 'saYa'] findall() digunakan untuk mencari semua pola yang cocok dengan teks dalam string dan mengembalikan hasilnya dalam bentuk list.
print(hasil3) #output = ['saya', 'Saya', 'saYa'] karena kita menggunakan re.I yang mengabaikan perbedaan antara huruf besar dan kecil, sehingga semua variasi dari "saya" dianggap cocok.

                            # 4. SUB() Mengganti teks
teks3 = "saya masih kuliah"
hasil4 = re.sub("kuliah", "bekerja", teks3) # Output: saya masih bekerja sub() digunakan untuk mengganti teks yang cocok dengan pola tertentu dengan teks baru dalam string.
print(hasil4)

                            # 5. SPLIT memotong string
teks4 = "Rasky,wijaya,sukses"
hasil5 = re.split(",", teks4) # Output: ['Rasky', 'wijaya', 'sukses'] split() digunakan untuk memotong string berdasarkan pola tertentu dan mengembalikan hasilnya dalam bentuk list.
print(hasil5)

