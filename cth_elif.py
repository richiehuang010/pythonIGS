suhu = float(input("Masukkan suhu udara (C) : "))
if suhu >= 35 :
    print("Cuaca sangat panas , minumlah air yang banyak")
elif suhu >= 25 :
    print("Cuaca hangat , cocok untuk beraktivitas di luar.")
elif suhu >= 15 :
    print("Cuaca sejuk , bawa jaket ringan.")
else :
    print("Cuaca dingin , kenakan jaket yang tebal.")