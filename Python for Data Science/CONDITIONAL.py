                                # CONDITIONAL = pengambilan keputusan dalam program

                                            
# Operator Perbandingan
    # Operator	Arti
        # >	lebih besar
        # <	lebih kecil
        # >=	lebih besar/sama
        # <=	lebih kecil/sama
        # ==	sama dengan
        # !=	tidak sama

# 1. IF - ELSE
umur = int(input("Masukkan umur Anda: "))

if umur >= 18:
    print("Boleh mengemudi")
else:
    print("Belum cukup umur")

# 2. IF - ELIF - ELSE
nilai = int(input("Masukkan nilai Anda: "))

if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")

# 3. Operator Logika

    # 1. AND = Semua kondisi harus benar
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login berhasil")
else:
    print("Login gagal")

    # 2. OR = Salah satu cukup benar
umur = 20
punya_sim = False

if umur >= 18 and punya_sim:
    print("Boleh menyetir")
else:
    print("Tidak boleh menyetir")

    # 3. not = kebalikan nya (negasi)
logged_in = False

if not logged_in:
    print("Silakan login dulu")


