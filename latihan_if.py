nilaiTugas = int(input("Masukkan nilai tugas : "))
nilaiUlangan= int(input("Masukkan nilai ulangan : "))
nilaiUjian = int(input("Masukkan nilai ujian : "))
if nilaiTugas > 100 or nilaiUjian > 100 or nilaiUlangan > 100 or nilaiTugas < 0 or nilaiUjian < 0 or nilaiUlangan < 0 :
    print("Mustahil")
else : 
    nilaiAkhir = (30/100 * nilaiTugas) + (30/100 * nilaiUlangan) + (40/100 * nilaiUjian)
    print(nilaiAkhir)
    if nilaiAkhir >= 90 : print("Sangat Baik")
    elif nilaiAkhir >= 75 : print("Baik")
    elif nilaiAkhir >= 60 : print("Cukup")
    else : print("Kurang")

#? mengambil 2 angka di blkg koma -> :.2f