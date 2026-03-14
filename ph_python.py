nama = input("Masukkan nama pelanggan : ")
umur = int(input("Masukkan umur pelanggan : "))
jumlah = int(input("Masukkan jumlah item : "))
harga = int(input("Masukkan harga per item : "))
harga_total = 0
harga_total += harga * jumlah
print(f"Total biaya {harga_total}")
hargaTambahan = harga_total + 50000
print(f"Harga dengan tambahan tetap {hargaTambahan}")
pajak = harga_total * 10/100
print(f"Pajak 10% {pajak}")
total_akhir = harga_total + 50000 + pajak
print(f"Total akhir {total_akhir}")
print(total_akhir > 500_000 or umur >= 20 )
print(f"Jumlah item wajar {jumlah >= 1 and jumlah <= 8 }")
print(f"apakah total biaya identik dengan biaya tambahan {harga_total is hargaTambahan}")



