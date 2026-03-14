jum = int(input("Masukkan jumlah siswa : "))
totalNilai = 0
for i in range(1,jum+1) :
    nilai = int(input(f"Masukkan nilai siswa-{i} : "))
    totalNilai += nilai
rata2 = totalNilai / jum
print(f"Rata-rata nilainya adalah {rata2}")