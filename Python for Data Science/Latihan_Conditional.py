# Latihan: Tingkat 1

# 1. Dapatkan masukan pengguna menggunakan masukan “Masukkan usia Anda: ”.
# Jika pengguna berusia 18 tahun ke atas, berikan masukan: Anda cukup umur untuk mengemudi.Jika dibawah 18 berikan feedback untuk menunggu jumlah tahun yang hilang.Keluaran:

umur = int(input("Masukkan usia Anda: "))

if umur >= 18:
    print("Anda cukup umur untuk mengemudi.")
else:
    print("Anda belum cukup umur untuk mengemudi, silakan tunggu", 18 - umur, "tahun lagi.")

# 2. Bandingkan nilai my_age dan your_age menggunakan if… else.
# Siapa yang lebih tua dari saya atau Anda?
# Gunakan input “Masukkan umur Anda: ” untuk mendapatkan umur sebagai masukan.
# Anda dapat menggunakan kondisi bersarang untuk mencetak 'tahun' untuk perbedaan usia 1 tahun, 'tahun' untuk perbedaan yang lebih besar, dan teks khusus jika usia_saya = usia_Anda.Keluaran:

my_age = 25
your_age = int(input("Masukkan umur Anda: "))

if your_age > my_age:
    selisih = your_age - my_age
    print(f"Anda {selisih} tahun lebih tua dari saya.")
elif your_age < my_age:
    selisih = my_age - your_age
    print(f"Saya {selisih} tahun lebih tua dari Anda.")
else:
    print("Umur kita sama.")

# 3. Dapatkan dua nomor dari pengguna menggunakan input prompt.
# Jika a lebih besar dari b maka hasil a lebih besar dari b, 
# jika a lebih kecil dari b maka hasil a lebih kecil dari b, 
# jika tidak a sama dengan b.Keluaran:

a = int(input("Masukkan angka a: "))
b = int(input("Masukkan angka b: "))

if a > b:
    print(f"{a} lebih besar dari {b}.")
elif a < b:
    print(f"{a} lebih kecil dari {b}.")
else:
    print(f"{a} sama dengan {b}.")

# Latihan Tingkat 2

# 1. Tuliskan kode yang memberikan nilai kepada siswa berdasarkan nilai mereka:

#     90-100, A
#     80-89, B
#     70-79, C
#     60-69, D
#     0-59, F

score = int(input("Masukkan nilai: "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")

# 2. Dapatkan bulan dari input pengguna lalu periksa apakah musimnya Musim Gugur, Musim Dingin, Musim Semi atau Musim Panas.Jika input pengguna adalah:
# September, Oktober atau November, musimnya adalah Musim Gugur.
# Desember, Januari atau Februari, musimnya adalah Musim Dingin.
# Maret, April atau Mei, musimnya adalah musim semi
# Juni, Juli atau Agustus, musimnya adalah Musim Panas


bulan = input('masukkan nama bulan:').strip().lower()

if bulan in ['september', 'oktober', 'november']:
    print('Musim Gugur')
elif bulan in ['desember', 'januari', 'februari']:
    print('Musim Dingin')
elif bulan in ['maret', 'april', 'mei']:
    print('Musim Semi')
elif bulan in ['juni', 'juli', 'agustus']:
    print('Musim Panas')
else:
    print('Nama bulan tidak valid')

# 3. Daftar berikut berisi beberapa buah-buahan:
#     fruits = ['banana', 'orange', 'mango', 'lemon']
# Jika buah tidak ada dalam daftar, tambahkan buah tersebut ke dalam daftar dan cetak daftar yang dimodifikasi.Jika buahnya ada, print 'Buah itu sudah ada di daftar'

buah = input("Masukkan nama buah: ")
list_buah = ['banana', 'orange', 'mango', 'lemon']

if buah in list_buah:
    print("Buah itu sudah ada di daftar.")
else:
    list_buah.append(buah)
    print("Daftar buah yang dimodifikasi:", list_buah)

# Latihan: Tingkat 3

# 1. Di sini kita memiliki kamus orang.Jangan ragu untuk memodifikasinya!

# ```python
person={
    'first_name': 'Vubceb',
    'last_name': 'babi',
    'age': 250,
    'country': 'indo',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# * Periksa apakah kamus orang tersebut memiliki kunci keterampilan, jika ada, cetaklah keterampilan tengah dalam daftar keterampilan.
# * Periksa apakah kamus orang tersebut memiliki kunci keterampilan, jika demikian periksa apakah orang tersebut memiliki keterampilan 'Python' dan cetak hasilnya.
# * Jika keterampilan seseorang hanya memiliki JavaScript dan React, cetak 'Dia adalah pengembang front end', jika keterampilan orang tersebut memiliki Node, Python, MongoDB, cetak 'Dia adalah pengembang backend', jika keterampilan orang tersebut memiliki React, Node dan MongoDB, Cetak 'Dia adalah pengembang fullstack', jika tidak, cetak 'judul tidak dikenal' - untuk hasil yang lebih akurat, lebih banyak kondisi dapat disarangkan!
# * Jika orang tersebut sudah menikah dan tinggal di indoia, cetak informasi dalam format berikut:

person = {
    'first_name': 'Vubceb',
    'last_name': 'babi',
    'age': 250,
    'country': 'indo',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Cek key 'skills' dan tampilkan skill tengah
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Skill tengah:", skills[middle_index]) #output: Node

# 2. Cek apakah ada skill Python
if 'skills' in person:
    print("Punya skill Python?", 'Python' in person['skills']) #output: True

# 3. Menentukan jenis developer
if 'skills' in person:
    skills = person['skills']
    
    if all(skill in skills for skill in ['JavaScript', 'React']) and len(skills) == 2:
        print('Dia adalah pengembang front end')
    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print('Dia adalah pengembang backend')
    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print('Dia adalah pengembang fullstack')
    else:
        print('Judul tidak dikenal')

# 4. Cek status menikah dan negara
if person.get('is_married') and person.get('country') == 'indo':
    print(f"{person['first_name']} {person['last_name']} tinggal di Indonesia dan sudah menikah.")