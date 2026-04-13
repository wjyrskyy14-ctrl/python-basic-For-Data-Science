# 1. Buat kamus kosong bernama dog
dog = {}

# 2. Tambahkan nama, warna, ras, kaki, umur ke kamus anjing
dog = {
    'nama' : 'shiroky',
    'warna' : 'hitam & putih',
    'ras' : 'siberian husky',
    'kaki' : 4,
    'umur' : '7 tahun'
}

# 3. Buat kamus siswa dan tambahkan nama depan, nama belakang, jenis kelamin, usia, status perkawinan, keterampilan, negara, kota dan alamat sebagai kunci kamus
siswa = {
    'nama depan' : 'Rasky',
    'nama belakang' : 'Wijaya',
    'jenis kelamin' : 'Laki - Laki',
    'usia' : 21,
    'status' : 'Single',
    'keterampilan' : ['Gitar', 'nyanyi', 'Yapping'],
    'tempat tinggal' : {
        'negara' : 'Indonesia',
        'kota' : 'Jakarta',
        'alamat' : 'Jl Ganteng Banget'
    }
}

# 4. Dapatkan panjang kamus siswa
print(len(siswa),'\n')

# 5. Dapatkan nilai skill dan periksa tipe datanya, harus berupa daftar
print(siswa['keterampilan'])
print(type(siswa['keterampilan']),'\n')

# 6. Ubah nilai keterampilan dengan menambahkan satu atau dua keterampilan
siswa['keterampilan'].extend(['berenang', 'makan']) #karna lebih dari satu skills makanya pakai extend
print(siswa,'\n')

# 7. Dapatkan kunci kamus sebagai daftar
print(siswa.keys(),'\n')

# 8. Dapatkan nilai kamus sebagai daftar
print(siswa.values(),'\n')


# 9. Ubah kamus menjadi daftar tupel menggunakan metode _items_
print(siswa.items(),'\n')

# 10. Hapus salah satu item/kunci dalam kamus
siswa.pop('umur')
print(siswa,'\n')

# 11. Hapus salah satu kamus
del dog
print(siswa)
