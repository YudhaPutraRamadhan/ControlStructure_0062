# Nomor 4

# Mengubah input dari pengguna menjadi tipe integer, sehingga bisa digunakan dalam operasi perulangan.
n = int(input("Masukkan nilai n: "))

# Menggunakan loop untuk mencetak angka ganjil
print("Angka ganjil hingga", n, ":")
for i in range(1, n + 1):
    # Memulai loop dari 1 hingga n, dengan 'n+1' agar angka 'n' juga diperiksa.
    if i % 2 != 0:
        # Memeriksa apakah 'i' adalah bilangan ganjil (sisa bagi dengan 2 tidak sama dengan 0).
        print(i)
        # Jika ganjil, mencetak nilai 'i'.
