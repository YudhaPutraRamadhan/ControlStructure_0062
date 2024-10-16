# Nomor 3

# Mengambil input dari pengguna dan mengubahnya menjadi tipe data integer untuk menentukan jumlah elemen deret Fibonacci yang akan dihitung.
n = int(input("Masukkan nilai n: "))
# Menginisialisasi dua variabel 'a' dan 'b' sebagai nilai awal deret Fibonacci (0 dan 1).
a, b = 0, 1
# Membuat list kosong 'hasil' yang akan menyimpan deret Fibonacci.
hasil = []

for i in range(n):
    hasil.append(a)
    # Memasukkan nilai 'a' ke dalam list 'hasil' sebagai elemen Fibonacci berikutnya.
    a, b = b, a + b
    # Menggeser nilai 'a' menjadi 'b', dan 'b' menjadi jumlah dari nilai sebelumnya ('a' + 'b').

# Menampilkan deret Fibonacci sesuai dengan jumlah 'n' yang diinputkan oleh pengguna.
print("Deret Fibonacci hingga", n, ":", hasil)