# import random
# kom = random.randint(1,100)
# while True :
#     user = int(input("Masukkan angka rahasia : "))
#     if user > kom : print("Error: Kapasitas terlalu besar.")
#     elif user < kom : print("Error: Kapasitas terlalu kecil.")
#     else :
#         print("Akses Diterima : Sever Telah Kembali.")
#         break

hero = ["batman","angela","superman","ling","xavier"]
update = []
user = input("masukkan hero yang terkena nerf : ")
if user in hero :
    hero.remove(user)
    newHero = input("masukkan hero baru yang sedang OP : ")
    hero.append(newHero)
    for i in range(3) : update.append(hero[i])
    update.sort()
    print(update)