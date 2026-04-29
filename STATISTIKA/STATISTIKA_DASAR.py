                # STATISTIKA DASAR (MEAN, MEDIAN, MODUS, MIN, MAX, STANDAR DEVIASI, VARIANS)

import numpy as np

# A. MEAN (RATA-RATA) jumlah data / banyak data
a = np.array([2,3,4,4,6])
print('nilai mean a:', np.mean(a),'\n') # hasilnya 3.8

# B. MEDIAN (NILAI TENGAH) urutkan data, lalu cari nilai tengahnya
a = np.array([2,5,2,4,4,2,3])
print("nilai median a :", np.median(a),'\n') # hasilnya 3

# C. MODUS (NILAI YG PALING SERING MUNCUL) urutkan data, lalu cari nilai yang paling sering muncul
a = np.array([2,5,2,4,4,4,2,3])
print("nilai modus a :", np.bincount(a).argmax(),'\n') # hasilnya 4

# D. MIN & MAX (NILAI TERKECIL & TERBESAR)
a = np.array([2,5,2,4,4,4,2,3])
print("nilai min a :", np.min(a)) # hasilnya 2
print("nilai max a :", np.max(a),'\n') # hasilnya 5


data = np.array([2,5,2,4,4,4,2,3])
# E. STANDAR DEVIASI (SEBARAN DATA DARI RATA-RATA) semakin besar standar deviasi, semakin jauh data dari rata-rata
# F. VARIANS (RATA RATA KUADRATSELISIH DATA TERHADAP MEAN) semakin besar varians, semakin jauh data dari rata-rata

print('nilai mean data:', np.mean(data)) # hasilnya 3.25
print('nilai standar deviasi data:', np.std(data)) # hasilnya 1.25
print('nilai varians data:', np.var(data),'\n') # hasilnya 1.5625
