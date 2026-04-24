                        # Simbol Regex yang WAJIB Hafal

import re

                                # DIGIT
# \d = angka (digit) [0-9]
re.findall("\d", "umur saya 21 tahun") # Output: ['2', '1']

                                # ANGKA UTUH
# \d+ = angka (digit) [0-9]
re.findall("\d+", "umur saya 21 tahun") # Output: ['21']

                                # DIMULAI DENGAN
# ^ = dimulai dengan
r'^Halo' # Output: <re.Match object; span=(0, 4), match='Halo'> pola ini digunakan untuk mencari teks yang dimulai dengan kata "Halo".

                                #DIAKHIRI DENGAN
# $ = diakhiri dengan
r'Rasky$' # Output: <re.Match object; span=(0, 5), match='Rasky'> pola ini digunakan untuk mencari teks yang diakhiri dengan kata "Rasky".

                                # NOL / BANYAK
# * = nol atau banyak
r'Rasky*' # Output: <re.Match object; span=(0, 5), match='Rasky'> pola ini digunakan untuk mencari teks yang mengandung kata "Rasky" diikuti oleh nol atau banyak karakter lainnya.

                                # MINIMAL 1
# + = minimal 1
r'Rasky+' # Output: <re.Match object; span=(0, 5), match='Rasky'> pola ini digunakan untuk mencari teks yang mengandung kata "Rasky" diikuti oleh minimal satu karakter lainnya.

                                # OPSIONAL
# ? = opsional
r'Rasky?' # Output: <re.Match object; span=(0, 5), match='Rasky'> pola ini digunakan untuk mencari teks yang mengandung kata "Rasky" diikuti oleh karakter lainnya yang bersifat opsional (boleh ada atau tidak ada).

                                # PILIHAN KARAKTER 
# [] = pilihan karakter
r'[Rr]asky' # Output: <re.Match object; span=(0, 5), match='Rasky'> pola ini digunakan untuk mencari teks yang mengandung kata "Rasky" atau "rasky", karena kita menggunakan [] untuk menentukan pilihan karakter R atau r.

                                # JUMLAH TERTENTU
# {n} = jumlah tertentu
r'Rasky{2}' # Output: <re.Match object; span=(0, 5), match='Rasky'> pola ini digunakan untuk mencari teks yang mengandung kata "Rasky" diikuti oleh tepat dua karakter lainnya.

                                
                                # Inti Besar Regex
                        # Regex biasanya dipakai untuk:

# validasi email
# validasi password
# validasi nomor HP
# cari angka
# cari tanggal
# cari kata tertentu
# bersihkan text
# web scraping
# data cleaning

# Makanya ini penting banget.
