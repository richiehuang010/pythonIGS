nilai_ujian = [75,55,90,85,45,95,80]
nilai_ujian.sort(reverse=True)
print(nilai_ujian)

nilai_ujian = [75,55,90,85,45,95,80]
nilai_ujian.sort(reverse=True)
print(nilai_ujian[:3])

nilai_ujian = [75,55,90,85,45,95,80]
for i in nilai_ujian :
    if i < 60 : nilai_ujian.remove(i)
print(nilai_ujian)