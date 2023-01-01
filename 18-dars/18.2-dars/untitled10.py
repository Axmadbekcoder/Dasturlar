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

for mahsulot, narx in bozorlik.items():
    print(f"{mahsulot.title()} {narx} so'm")