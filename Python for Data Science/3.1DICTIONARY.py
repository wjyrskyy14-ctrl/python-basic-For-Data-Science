                         # DICTIONARY / KAMUS = kumpulan data dalam bentuk pasangan KEY : VALUE

# 1. DICTIONARY KOSONG
dog = {}

# 2. DICTIONARY BERISI DATA 
data = {
    'NAMA' : 'RASKY',
    'UMUR' : 21,
    'NEGARA' : 'INDONESIA'
}
print(data,'\n') #output = {'NAMA': 'RASKY', 'UMUR': 21, 'NEGARA': 'INDONESIA'}

# 3. MENGHITUNG PANJANG DICTIONARY
print(len(data),'\n') #output = 3

# 4. Mengakses Data Dictionary
print(data['NAMA'],'\n') #output = RASKY

# 5. Menambah Data Baru
data['PEKERJAAN'] = 'DATA SCIENTIST'
print(data, '\n') #output = {'NAMA': 'RASKY', 'UMUR': 21, 'NEGARA': 'INDONESIA', 'PEKERJAAN': 'DATA SCIENTIST'}

# 6. Mengubah Data
data['NAMA'] = 'RASKY WIJAYA'
print(data,'\n') #output = {'NAMA': 'RASKY WIJAYA', 'UMUR': 21, 'NEGARA': 'INDONESIA', 'PEKERJAAN': 'DATA SCIENTIST'}

# 7. Cek Key Ada atau Tidak
print('NAMA' in data, '\n') #output = TRUE

# 8. Menghapus Data
    
    # 1. Menghapus Data Berdasarkan KEY
data.pop("UMUR")
print(data) #output = {'NAMA': 'RASKY WIJAYA', 'NEGARA': 'INDONESIA', 'PEKERJAAN': 'DATA SCIENTIST'} Umur hilang

    # 2. Hapus item terakhir
data.popitem()
print(data, '\n') #output = {'NAMA': 'RASKY WIJAYA', 'NEGARA': 'INDONESIA'} pekerjaan hilang karna dalam DICT, KEY pekerjaan paling akhir

# 9. Ambil Semua Key / Value / Item
    # 1. Semua Key
print(data.keys()) #output = dict_keys(['NAMA', 'NEGARA'])

    # 2. semua value
print(data.values()) #output = dict_values(['RASKY WIJAYA', 'INDONESIA'])

    # 3. ambil KEY & VALUES
print(data.items(),'\n') #output = dict_items([('NAMA', 'RASKY WIJAYA'), ('NEGARA', 'INDONESIA')]

# 10. Copy Dictionary
data_copy = data.copy()
data_copy['UMUR'] = 21 #menambahkan KEY VALUES tpi hanya ke datacopy
data_copy['PEKERJAAN'] = 'DATA SCIENTIST' #menambahkan KEY VALUES tpi hanya ke datacopy
print(data_copy) #output = {'NAMA': 'RASKY WIJAYA', 'NEGARA': 'INDONESIA', 'UMUR': 21, 'PEKERJAAN': 'DATA SCIENTIST'}
print(data, '\n') #output = {'NAMA': 'RASKY WIJAYA', 'NEGARA': 'INDONESIA'} ttp karna ini data asli nya bukan copy 

# 11. Clear vs Del
    
    # 1. CLEAR
data.clear() # isi DICT hilang
print(data) #output = {}

    # 2. DEL 
# del data
# print(data, '\n') #output = ERROR

                                #Dictionary Bisa Menyimpan Apa Saja?

student = {
    'NAMA' : 'RASKY WIJAYA',
    'UMUR' : 21,
    'KELAS' : '2IA10',
    'SKILS' : ['PYTHON', 'PANDAS', 'MACHINE LEARNING', 'DEEP LEARNING'],
    'ALAMAT' : {
        'nama jalan' : 'Jl Rasvira',
        'kode pos' : 656465,
        'Kota' : 'Jakarta'
    }
}

#kesimpulan = bisa menyimpan semua tipe data 

print(student)
