umur = int(input("Masukkan umur pengunjung : "))
tinggi = int(input("Masukkan tinggi badan (cm) : "))
if umur >= 10 :
    print("Boleh naik wahana.")
    if tinggi >= 130 :
        print("Kategori : Wahana Ekstrem")
    else : print("Kategori : Wahana anak-anak")
else : print("Maaf , belum boleh naik wahana")