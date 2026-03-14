# for jam in range(1,7) :        
#     print(f"Lonceng berbunyi untuk jam ke-{jam}!")

# hitungan = 5
# while hitungan >= 1 :
#     print(f"Hitungan mundur {hitungan}")
#     hitungan -= 1
# print("Roket diluncurkan !")

# hari = 1
# total = 0

# while total <= 100_000 :
#     total += 10_000
#     total += total * 10/100
#     print(f"Hari ke-{hari} : total = {int(total)}")
#     hari += 1
# print(f"Tabungan mencapai 100.000 atau lebih pada hari ke-{hari-1}")

for baris in range(1,6) :
    print(f"Baris {baris} : ",end=" ")
    for kursi in range(1,7) :
        print(f"[{kursi}]",end=" ")
    print()