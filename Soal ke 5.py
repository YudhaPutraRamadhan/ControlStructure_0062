#Nomer 5

# Mengambil input dari pengguna dan mengonversinya menjadi tipe data integer untuk menentukan jumlah baris.
n = int(input("Masukkan nilai n: "))

# Menggunakan loop untuk mencetak desain angka
for i in range(1, n + 1):
    # Loop pertama mengontrol baris dari 1 hingga n.
    for j in range(i):
        # Loop kedua mengontrol jumlah angka yang dicetak pada setiap baris, sesuai dengan nilai 'i'.
        print(i, end=" ")
        # Mencetak angka 'i' di setiap iterasi pada baris yang sama, diakhiri dengan spasi (tanpa pindah baris).
    print()
    # Memindahkan ke baris baru setelah selesai mencetak satu baris angka.
