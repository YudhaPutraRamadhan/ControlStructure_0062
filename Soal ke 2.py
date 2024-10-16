# Nomor 2

# Meminta pengguna untuk memasukkan angka pertama, angka kedua, dan angka ketiga, lalu mengubah input menjadi tipe float
Angka_Pertama = float(input("Masukkan Angka Pertama:"))
Angka_Kedua = float(input("Masukkan Angka Kedua: "))
Angka_Ketiga = float(input("Masukkan Angka Ketiga: "))

# Mengecek apakah Angka_Pertama adalah yang terbesar dibandingkan dengan Angka_Kedua dan Angka_Ketiga
if Angka_Pertama >= Angka_Kedua and Angka_Pertama >= Angka_Ketiga:
    largest = Angka_Pertama
# Mengecek apakah Angka_Kedua lebih besar atau sama dengan Angka_Pertama dan Angka_Ketiga
elif Angka_Kedua >= Angka_Pertama and Angka_Kedua >= Angka_Ketiga:
    largest = Angka_Kedua
# Jika kondisi lain tidak terpenuhi, berarti Angka_Ketiga adalah yang terbesar
else:
    largest = Angka_Ketiga

# Menampilkan hasil angka terbesar dari ketiga angka yang dimasukkan tadi
print(f"Angka Terbesar adalah : {largest}")