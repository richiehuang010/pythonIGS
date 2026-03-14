nama_siswa = ["Andi","Budi","Citra"]
nilai = [80,75,90]
print(nama_siswa[0])

buah = ["apel","pisang"]
buah.append("jeruk")
print(buah)
buah.insert(1,"mangga")
print(buah)

# ? menggabungkan 2 list -> .extend()
buah1 = ["apel","pisang"]
buah2 = ["jeruk","anggur"]
buah1.extend(buah2)
print(buah1)

buah = ["apel","pisang","jeruk"]
# buah.remove("pisang")
# print(buah)
buah.pop(1)
print(buah)

# todo JIKA .pop() saja () tanpa isi , maka index terakhir akan terhapus
# todo .clear() untuk menghapus semua elemen dlm arr