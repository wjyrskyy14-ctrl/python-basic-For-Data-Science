                                        # Date Time

from datetime import datetime

# 1. Ambil waktu sekarang
now = datetime.now()

print('contoh ambil waktu sekarang :')
print(now) #tanggal dan waktu sekarang
print(now.day) #tanggal
print(now.month) #bulan
print(now.year) #tahun
print(now.hour) #jam
print(now.minute) #menit
print(now.timestamp(),'\n') #timestamp adalah jumlah detik sejak 1 januari 1970

# 2. FORMAT WAKTU (biar rapih)
format_waktu = now.strftime('%d-%m-%Y %H:%M:%S') #format waktu yang diinginkan

print('contoh format waktu :')
print(format_waktu,'\n') #outputnya akan sesuai dengan format yang kita buat

                                        # ARTI SIMBOL NYA :
# %d : tanggal
# %m : bulan
# %Y : tahun
# %H : jam (24 jam)
# %M : menit
# %S : detik

# 3. UBAH STRING MENJADI WAKTU 
"27 April, 2025" #contoh string yang ingin diubah menjadi waktu

date_string = "27 April, 2025"
date_object = datetime.strptime(date_string, '%d %B, %Y') #ubah string menjadi waktu dengan format yang sesuai

print(date_object,'\n')

# 4. SELISIH WAKTU 

born = datetime(2005, 4, 27) #tanggal lahir

selisih = now - born #selisih waktu antara sekarang dan tanggal lahir
print(selisih)

                                                
                                                # RINGKASAN

# | Fungsi         | Kegunaan             |
# | -------------- | -------------------- |
# | datetime.now() | ambil waktu sekarang |
# | strftime()     | format waktu         |
# | strptime()     | string → waktu       |
# | timedelta      | selisih waktu        |
