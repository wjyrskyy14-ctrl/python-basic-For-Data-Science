                    #Modul Bawaan Python (INI YANG SERING KELUAR)

                                    # A MATEMATIKA :
import math
    # example
print('contoh penggunaan modul matematika')
print(math.sqrt(16))  # Output: 4.0 sqrt() digunakan untuk menghitung akar kuadrat dari suatu angka.
print(math.pi,'\n')  # Output: 3.141592653589793 pi adalah konstanta matematika yang mewakili rasio keliling lingkaran terhadap diameternya.

                                    # B STATISTIKA :
import statistics
    # example
data =[1,2,3,4,6,6,6,6,7,7,7,9,10]

print('contoh penggunaan modul statistika')
print(statistics.mode(data))  # Output: 6 modus() digunakan untuk menghitung nilai yang paling sering muncul dalam suatu kumpulan data.
print(statistics.mean(data))  # Output: 5.846153846153846 mean() digunakan untuk menghitung rata-rata dari suatu kumpulan data.
print(statistics.median(data),'\n')  # Output: 6 median() digunakan untuk menghitung nilai tengah dari suatu kumpulan data.

                                    # C DATE TIME :
import datetime
    # example
print('contoh penggunaan modul date time')
print(datetime.datetime.now()) # Output: 2024-06-01 12:34:56.789012 (contoh output, akan berbeda setiap kali dijalankan) now() digunakan untuk mendapatkan tanggal dan waktu saat ini.
