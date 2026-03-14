y = 1
jumLampuMenyala = 0
ruangan = ""
while y <= 5:
    if y == 1:  ruangan = "Ruang Tamu"
    elif y == 2: ruangan = "Dapur"
    elif y == 3: ruangan = "Kamar 1"
    elif y == 4: ruangan = "Kamar 2"
    else :  ruangan = "Kamar Mandi"
    kondisi = int(input(f"Masukkan kondisi lampu di {ruangan} (1=nyala, 0=mati) : "))
    if kondisi == 1:
        jumLampuMenyala += 1
    y += 1

print(f"Jumlah lampu yg menyala ada {jumLampuMenyala}")

if jumLampuMenyala > 2:
    print("Hemat listrik! Terlalu banyak lampu menyala")
else:
    print("Penggunaan listrik sudah baik")
