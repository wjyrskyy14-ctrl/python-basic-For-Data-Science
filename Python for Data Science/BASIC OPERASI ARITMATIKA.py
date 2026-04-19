a = 10
b = 3

print(a + b)   # tambah
print(a - b)   # kurang
print(a * b)   # kali
print(a / b)   # bagi (hasil float)
print(a // b)  # bagi bulat
print(a % b)   # sisa bagi
print(a ** b)  # pangkat

# Program kalkulator sederhana
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

operasi = input("Masukkan operasi (+, -, *, /, //, %, **): ")

if operasi == "+":
    hasil = a + b
elif operasi == "-":
    hasil = a - b
elif operasi == "*":
    hasil = a * b
elif operasi == "/":
    hasil = a / b
elif operasi == "//":
    hasil = a // b
elif operasi == "%":
    hasil = a % b
elif operasi == "**":
    hasil = a ** b
else:
    print("Operasi tidak dikenal!")
    exit()

print("Hasil:", hasil)

