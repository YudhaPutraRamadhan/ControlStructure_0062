# Nomor 1
#Fungsi untuk mengevaluasi performa siswa
persen = float(input("Masukkan Nilai :"))

if persen >= 90: #Memeriksa inputan nilainya, jika nilai 90 atau lebih dari 90, maka akan mengeluarkan output "Performa Sangat Baik" 
    print ("performa Sangat baik")
elif persen >=80: #Memeriksa inputan nilainya, jika nilai 80 atau lebih dari 80, maka akan mengeluarkan output "Performa Baik" 
    print ("Performa Baik")
elif persen >= 70: #Memeriksa inputan nilainya, jika nilai 70 atau lebih dari 70, maka akan mengeluarkan output "Performa Cukup Baik" 
    print ("Performa Cukup baik")
elif persen >= 60: #Memeriksa inputan nilainya, jika nilai 60 atau lebih dari 60, maka akan mengeluarkan output "Performa Rata-Rata" 
    print ("Performa Rata-Rata")
else:
    print ("Tingkatkan lagi nilaimu!") #Jika nilainya kurang dari 60, maka akan mengeluarkan output "Tingkatkan lagi nilaimu!"
 