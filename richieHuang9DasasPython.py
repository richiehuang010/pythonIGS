jumRombongan = int(input("Masukkan jumlah rombongan : "))
i = 1
diskon = 0
pendapatan = 0
while i <= jumRombongan : 
    namaRombongan = input(f"Masukkan nama rombongan {i} : ")
    jumOrg = int(input(f"Masukkan jumlah orang di rombongan {i} : "))
    if jumOrg > 10 : tiketGratis = 3
    elif jumOrg >= 7 and jumOrg <= 10 : tiketGratis = 2
    elif jumOrg >= 4 and jumOrg <= 6 :  tiketGratis = 1
    else : tiketGratis = 0

    jumOrgYgBayar = (jumOrg - tiketGratis)  * 50_000
    HargaSebelumDiskon = (jumOrg - tiketGratis)  * 50_000

    if jumOrgYgBayar > 400_000 :  diskon = 8
    else : diskon = 0
    harga = (100 - diskon) / 100 * jumOrgYgBayar    
    potonganHarga = diskon * harga
    pendapatan += harga

    print(f'''
        Nama : {namaRombongan}
        Jumlah orang : {jumOrg}
        Bonus tiket : {tiketGratis}
        Harga sebelum diskon : {HargaSebelumDiskon}
        Potongan harga : {potonganHarga}
        Total yang harus dibayar : {harga}
    ''')
    i += 1
        
print(f'''
==========
Total pendapatan bioskop adalah {pendapatan}
''')