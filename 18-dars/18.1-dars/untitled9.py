mahsulotlar=[]
print("Hurmatli foydalanuvchi, siz qanday mahsulot buyurma qilmoqchisiz?")
n=1 # mahsulotlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-mahsulot nomini kiriting:"
    mahsulot = input(savol)
    mahsulotlar.append(mahsulot)
    javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break