nilai = int(input("Masukkan nilai Anda: "))

if 90 <= nilai <= 100:
    print("Lulus sangat baik")
elif 75 <= nilai <= 89:
    print("Lulus")
elif 0 <= nilai <= 74:
    print("Tidak lulus")
else:
    print("Nilai tidak valid")
