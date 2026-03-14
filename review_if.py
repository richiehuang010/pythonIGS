harga = int(input("Masukkan harga 1 buku : "))
jum = int(input("Masukkan jumlah buku : "))
harga_akhir = harga * jum
if jum > 5 :
    diskon = 20/100
elif jum >= 3 and jum <= 5 :
    diskon = 10/100
else : diskon = 0

print(f"Harga sebelum diskon : {harga_akhir}")
potongan = 1 - diskon
print(f"Besar diskon ({diskon}) : {diskon * harga_akhir}")
print(f"Harga setelah diskon : {potongan * harga_akhir}")