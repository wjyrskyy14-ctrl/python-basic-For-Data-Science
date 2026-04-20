                    # cara import modul dengan nama modul

import Modul_1
print('import modul dengan nama modul')
print(Modul_1.tambah(2, 3))  # Output: 5
print(Modul_1.kali(4, 5),'\n')    # Output: 20

                    # cara import modul yg lebih gampang 

from Modul_1 import tambah, kali
print('import modul dengan nama fungsi / versi gampang')
print(tambah(2, 3))  # Output: 5
print(kali(4, 5),'\n')    # Output: 20

                    # cara import modul dengan alias

from Modul_1 import tambah as t, kali as k
print('contoh import modul dengan alias')
print(t(2, 3))  # Output: 5
print(k(4, 5),'\n')    # Output: 20
