# WEB SCRAPPING = mengambil data dari website menggunakan program Python

# cara kerja nya = misal kalian ingin mengambil daftar film dari website, kalau manual kita copy satu satu.
#                  Dengan web scrapping kita bisa membuat program untuk mengambil data tersebut secara otomatis, sehingga lebih cepat dan efisien. 

# TOOLS YG DIPAKAI : REQUEST & BEAUTIFULSOUP

#MEMBUKA PINTU KE WEBSITE TERLEBIH DAHULU AGAR BISA DI CODING 

import requests # import library request untuk melakukan permintaan HTTP ke website
from bs4 import BeautifulSoup  # import library BeautifulSoup untuk memparsing HTML dan mengambil data dari website

url = "https://id.wikipedia.org/wiki/Anjing" # URL yang ingin kita scrapping, dalam hal ini adalah halaman Wikipedia tentang Anjing

# Wikipedia wajib pakai User-Agent
headers = {
    'User-Agent': 'BelajarPython/1.0 (Kontak: emailanda@example.com)'
} #headers ini digunakan untuk memberi tahu server bahwa permintaan ini berasal dari program kita, bukan dari browser biasa. Ini penting karena beberapa situs web mungkin memblokir permintaan yang tidak memiliki User-Agent yang valid.

response = requests.get(url, headers=headers) # Mengirim permintaan GET ke URL dengan header yang sudah ditentukan, dan menyimpan responsenya dalam variabel response

print('status code:', response.status_code) # Menampilkan status code dari responsenya, yang menunjukkan apakah permintaan berhasil (200) atau tidak") 

if response.status_code == 200: # Jika status code adalah 200, berarti permintaan berhasil dan kita bisa melanjutkan untuk memparsing HTML-nya
    soup = BeautifulSoup(response.text, 'html.parser') # Membuat objek BeautifulSoup dengan menggunakan teks HTML dari response dan parser 'html.parser' untuk memparsing HTML tersebut. Objek soup ini akan digunakan untuk mengambil data dari halaman web.
    # Mengambil judul utama artikel (h1)
    judul = soup.find('h1').text # Menggunakan metode find() untuk mencari elemen <h1> pertama dalam HTML, yang biasanya berisi judul utama artikel. Kemudian, menggunakan .text untuk mengambil teks dari elemen tersebut dan menyimpannya dalam variabel judul.
    print(f"Berhasil mengakses halaman: {judul}") 
else:
    print("Masih diblokir oleh Wikipedia")

# 1. MENGAMBIL ISI HTML (masih berantakan alias masih pake bahasa HTML)
print(response.text)

# 2. AMBIL JUDUL WEBSITE MENGGUNAKAN BEAUTIFULSOUP (agar lebih enak dan mudah dibaca)
soup = BeautifulSoup(response.text, 'html.parser') # Membuat objek BeautifulSoup dengan menggunakan teks HTML dari response dan parser 'html.parser' untuk memparsing HTML tersebut. Objek soup ini akan digunakan untuk mengambil data dari halaman web.

print("contoh soup.title:")
print(soup.title,'\n') # Ini mengambil seluruh elemen HTML beserta tag-nya

print("contoh soup.title.text:")
print(soup.title.text) # hanya mengambil teks murni judul nya 

# 3. CARI SEMUA LINK DALAM WEBSITE
link = soup.find_all('a') # Menggunakan metode find_all() untuk mencari semua elemen <a> dalam HTML, yang biasanya digunakan untuk membuat tautan (link). Hasilnya akan berupa daftar (list) dari semua elemen <a> yang ditemukan.

print("contoh link:")
for a in link:
    print(a.text)

# 4. CARI SEMUA PARAGRAF DALAM WEBSITE
paragraf = soup.find_all('p') # Menggunakan metode find_all() untuk mencari semua elemen <p> dalam HTML, yang biasanya digunakan untuk membuat paragraf. Hasilnya akan berupa daftar (list) dari semua elemen <p> yang ditemukan.

print("contoh paragraf:")
for p in paragraf:
    print(p.text)

                                            
                                            # Inti Materi Ini
# Hafalkan ini:

# requests.get() : ambil website
# response.status_code : cek berhasil atau tidak
# response.text : lihat isi HTML
# BeautifulSoup() : ubah HTML agar mudah dibaca
# find() : cari satu data
# find_all() : cari banyak data
