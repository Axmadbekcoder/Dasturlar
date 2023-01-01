mahsulotlar=['non', 'baliq']
print("Qanday mahsulot hohlaysiz?")
bozorlik = {}
ishora = True
while ishora:
    mahsulot = input("Mahsulot nomini kiritng : ")
    narx = input(f"{mahsulot.title()}ning narxiini kiriting: ")
    bozorlik[mahsulot] = int(narx) # mahsulot kalit, narx qiymat
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

while mahsulotlar:
    mahsulot1 = mahsulotlar.pop()
    if mahsulot1 in bozorlik.keys():
        narh = bozorlik[mahsulot1]
        print(f"{mahsulot1.title()} - {narh} so'm")
    else:
        print(f"Bizda {mahsulot} yo'q")
        